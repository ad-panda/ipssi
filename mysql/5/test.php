<?php
require_once "config.php";

$sort = $_GET["sort"] ?? "nom";
$order = $_GET["order"] ?? "asc";

if (!in_array($sort, ["nom","pays","course","temps","classement"])) die("Invalid sort");
if (!in_array($order, ["asc","desc"])) die("Invalid order");

$errors = [];

if (!empty($_POST["submit"])) {
    $pays = strtoupper(trim($_POST["pays"]));
    if (!preg_match("/^[A-Z]{3}$/", $pays)) {
        $errors[] = "Le pays doit être composé de 3 lettres majuscules (ex : FRA).";
    }

    if (!is_numeric($_POST["temps"])) {
        $errors[] = "Le temps doit être un nombre.";
    }

    if (empty($errors)) {
        $sthAdd = $dbh->prepare("INSERT INTO jo.`100` (nom,pays,course,temps)
                                VALUES (:nom,:pays,:course,:temps)");
        $sthAdd->execute([
            "nom" => $_POST["nom"],
            "pays" => $pays,
            "course" => $_POST["course"],
            "temps" => $_POST["temps"]
        ]);

        header("Location: test.php");
        exit;
    }
}

$searchSQL = "";
$params = [];

if (!empty($_GET["search"])) {
    $searchSQL = " WHERE nom LIKE :s OR pays LIKE :s OR course LIKE :s ";
    $params["s"] = "%" . $_GET["search"] . "%";
}

$limit = 10;
$page = isset($_GET["page"]) ? intval($_GET["page"]) : 1;
$offset = ($page - 1) * $limit;

$count = $dbh->prepare("SELECT COUNT(*) FROM jo.`100` $searchSQL");
$count->execute($params);
$total = $count->fetchColumn();
$totalPages = ceil($total / $limit);

$sth = $dbh->prepare("
    SELECT * FROM jo.`100`
    $searchSQL
    ORDER BY $sort $order
    LIMIT $limit OFFSET $offset
");

$sth->execute($params);
$data = $sth->fetchAll(PDO::FETCH_ASSOC);

$courses = [];
foreach ($data as $row) {
    $courses[$row["course"]][] = $row;
}

foreach ($courses as &$rows) {
    usort($rows, function($a, $b) { return $a["temps"] <=> $b["temps"]; });
    $rank = 1;
    foreach ($rows as &$r) {
        $r["classement"] = $rank++;
    }
}

$data = [];
foreach ($courses as $rows) {
    foreach ($rows as $r) $data[] = $r;
}

echo "<h2>Ajouter un résultat</h2>";

if (!empty($errors)) {
    foreach ($errors as $e) echo "<p style='color:red;'>$e</p>";
}

echo '
<form method="post">
    Nom : <input type="text" name="nom" required><br><br>
    Pays (ex : FRA) : <input type="text" name="pays" maxlength="3" required><br><br>
    Course : 
<select name="course" required>
    <option value="">--Choisir une course--</option>
    <option value="Championnats du monde Eugene 2022">Championnats du monde Eugene 2022</option>
    <option value="Championnats du monde d\'athlétisme 2023">Championnats du monde d\'athlétisme 2023</option>
    <option value="JO 2008">JO 2008</option>
    <option value="JO 2012">JO 2012</option>
    <option value="JO 2020">JO 2020</option>
</select><br><br>
    Temps : <input type="text" name="temps" required><br><br>
    <input type="submit" name="submit" value="Ajouter">
</form>
<hr>
';

echo '
<form method="get">
    <input type="text" name="search" placeholder="Rechercher..." value="'.($_GET["search"] ?? '').'">
    <button type="submit">OK</button>
</form>
<hr>
';

echo "<table border='1' cellpadding='5'>
<thead>
<tr>

<th>
Nom 
<a href='./test.php?sort=nom&order=asc' style='color:".($sort=='nom' && $order=='asc' ? "red" : "black")."'>↑</a>
<a href='./test.php?sort=nom&order=desc' style='color:".($sort=='nom' && $order=='desc' ? "red" : "black")."'>↓</a>
</th>

<th>
Pays
<a href='./test.php?sort=pays&order=asc' style='color:".($sort=='pays' && $order=='asc' ? "red" : "black")."'>↑</a>
<a href='./test.php?sort=pays&order=desc' style='color:".($sort=='pays' && $order=='desc' ? "red" : "black")."'>↓</a>
</th>

<th>
Course
<a href='./test.php?sort=course&order=asc' style='color:".($sort=='course' && $order=='asc' ? "red" : "black")."'>↑</a>
<a href='./test.php?sort=course&order=desc' style='color:".($sort=='course' && $order=='desc' ? "red" : "black")."'>↓</a>
</th>

<th>
Temps
<a href='./test.php?sort=temps&order=asc' style='color:".($sort=='temps' && $order=='asc' ? "red" : "black")."'>↑</a>
<a href='./test.php?sort=temps&order=desc' style='color:".($sort=='temps' && $order=='desc' ? "red" : "black")."'>↓</a>
</th>

<th>
Classement
<a href='./test.php?sort=classement&order=asc' style='color:".($sort=='classement' && $order=='asc' ? "red" : "black")."'>↑</a>
<a href='./test.php?sort=classement&order=desc' style='color:".($sort=='classement' && $order=='desc' ? "red" : "black")."'>↓</a>
</th>

<th>Modifier</th>

</tr>
</thead>";


foreach ($data as $valeur) {
    echo "<tr>
        <td>{$valeur["nom"]}</td>
        <td>{$valeur["pays"]}</td>
        <td>{$valeur["course"]}</td>
        <td>{$valeur["temps"]}</td>
        <td>{$valeur["classement"]}</td>
        <td><a href='edit.php?id={$valeur["id"]}'>Modifier</a></td>
    </tr>";
}

echo "</table><br>";

for ($i = 1; $i <= $totalPages; $i++) {
    echo "<a href='?page=$i&sort=$sort&order=$order&search=".($_GET["search"] ?? "")."'> $i </a> ";
}

$dbh = null;
?>
