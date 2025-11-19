<?php
require_once "config.php";

if (!isset($_GET["id"])) {
    die("ID manquant dans l’URL.");
}

$id = intval($_GET["id"]);

$sth = $dbh->prepare("SELECT * FROM jo.`100` WHERE id = :id");
$sth->execute(["id" => $id]);
$data = $sth->fetch(PDO::FETCH_ASSOC);

if (!$data) {
    die("Coureur introuvable.");
}

$errors = [];

if (!empty($_POST["submit"])) {
    $pays = strtoupper(trim($_POST["pays"]));
    if (!preg_match("/^[A-Z]{3}$/", $pays)) {
        $errors[] = "Le pays doit contenir exactement 3 lettres majuscules (ex : FRA).";
    }

    if (!is_numeric($_POST["temps"])) {
        $errors[] = "Le temps doit être un nombre.";
    }

    if (empty($errors)) {
        $sthUpdate = $dbh->prepare("
            UPDATE jo.`100`
            SET nom = :nom,
                pays = :pays,
                course = :course,
                temps = :temps
            WHERE id = :id
        ");

        $sthUpdate->execute([
            "nom"   => $_POST["nom"],
            "pays"  => $pays,
            "course"=> $_POST["course"],
            "temps" => $_POST["temps"],
            "id"    => $id
        ]);

        header("Location: test.php");
        exit;
    }
}
?>

<h2>Modifier un coureur</h2>

<?php
foreach ($errors as $e) {
    echo "<p style='color:red;'>$e</p>";
}
?>

<form method="post">
    Nom :  
    <input type="text" name="nom" value="<?= $data['nom'] ?>" required><br><br>

    Pays (FRA) :  
    <input type="text" name="pays" maxlength="3" value="<?= $data['pays']?>" required><br><br>

    Course :  
    <input type="text" name="course" value="<?= $data['course'] ?>" required><br><br>

    Temps :  
    <input type="text" name="temps" value="<?= $data['temps'] ?>" required><br><br>

    <button type="submit" name="submit">Modifier</button>
</form>

<br>
<a href="test.php">⬅ Retour</a>
