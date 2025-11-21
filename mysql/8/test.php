<?php
session_start();
require_once "config.php";

// ---- Tri colonnes ----
$sort = "id";
if (isset($_GET["sort"])) {
  $sort = $_GET["sort"];
}

$order = "asc";
if (isset($_GET["order"])) {
  $order = $_GET["order"];
}

if(!in_array($sort, ["id","username","password"])) {
  die("Invalid sort");
}

if(!in_array($order, ["asc","desc"])) {
  die("Invalid order");
}

// ---- INSCRIPTION ----
if(isset($_POST['register'])){
  if(!empty($_POST['username']) && !empty($_POST['password'])){

    $hash = password_hash($_POST['password'], PASSWORD_DEFAULT);

    $sth = $dbh->prepare("
        INSERT INTO jo.user (username, password)
        VALUES (:username, :password)
    ");

    $sth->execute([
      'username' => $_POST['username'],
      'password' => $hash,
    ]);

    echo '<b>Votre inscription est valide</b>';
  }
}

// ---- CONNEXION ----
if(isset($_POST['connect'])){
  if(!empty($_POST['username']) && !empty($_POST['password'])){

    $stmt = $dbh->prepare("SELECT * FROM jo.user WHERE username = :username");
    $stmt->execute(['username' => $_POST['username']]);

    $user = $stmt->fetch(PDO::FETCH_ASSOC);

    if ($user && password_verify($_POST['password'], $user['password'])) {
        $_SESSION['name'] = $user['username'];
        $_SESSION['counter'] = $_SESSION['counter'] ?? 0;
    } else {
        echo "<b>Identifiants incorrects</b>";
    }
  }
}

// ---- DECONNEXION ----
if(isset($_POST["button"])) { 
  unset($_SESSION["name"]);
  unset($_SESSION["counter"]);
}

// ---- Tableau des utilisateurs ----
$sth=$dbh->prepare("SELECT * FROM jo.user ORDER BY $sort $order");
$sth->execute();
$data = $sth->fetchAll(PDO::FETCH_ASSOC);

// ---- SI CONNECTÉ ----
if (isset($_SESSION["name"])) {

  $_SESSION["counter"]++;

  echo '
  <h1>L\'utilisateur '.$_SESSION["name"].' est connecté pour la '.$_SESSION["counter"].'ème fois</h1>
  <form action="test.php" method="POST">
    <input type="submit" value="deconnexion" name="button">
  </form>
  ';

} else {

  echo '
  <h1>Login interne</h1>
  <form action="test.php" method="POST">
    <label>Nom temporaire : </label>
    <input type="text" id="visitor_name" name="visitor_name">
    <input type="submit" value="Entrer">
  </form>
  ';

  // pour le compteur local
  if(isset($_POST["visitor_name"])) {
    $_SESSION["name"] = $_POST["visitor_name"];
    $_SESSION["counter"] = 0;
  }
}

// ---- FORMULAIRE INSCRIPTION + CONNEXION ----
echo '
<h1>Inscription</h1>
<form action="test.php" method="POST">
  <label>Username</label>
  <input type="text" name="username">
  <br>
  <label>Password</label>
  <input type="text" name="password">
  <br>
  <input type="submit" value="valider" name="register">
</form>

<br>

<h1>Connexion</h1>
<form action="test.php" method="POST">
  <label>Username</label>
  <input type="text" name="username">
  <br>
  <label>Password</label>
  <input type="text" name="password">
  <br>
  <input type="submit" value="valider" name="connect">
</form>
';

// ---- TABLEAU ----
echo "<table>
<thead>
<tr>
<th>ID 
<a style='" . ($sort=='id' && $order=='asc'?'color:red':'') . "' href='./test.php?sort=id&order=asc'>↑</a> 
<a style='" . ($sort=='id' && $order=='desc'?'color:red':'') . "' href='./test.php?sort=id&order=desc'>↓</a>
</th>
<th>Username 
<a style='" . ($sort=='username' && $order=='asc'?'color:red':'') . "' href='./test.php?sort=username&order=asc'>↑</a> 
<a style='" . ($sort=='username' && $order=='desc'?'color:red':'') . "' href='./test.php?sort=username&order=desc'>↓</a>
</th>
<th>Password 
<a style='" . ($sort=='password' && $order=='asc'?'color:red':'') . "' href='./test.php?sort=password&order=asc'>↑</a> 
<a style='" . ($sort=='password' && $order=='desc'?'color:red':'') . "' href='./test.php?sort=password&order=desc'>↓</a>
</th>
</tr>
</thead>";

foreach($data as $value){
  echo "<tr>
  <td>".$value["id"]."</td>
  <td>".$value["username"]."</td>
  <td>".$value["password"]."</td>
  </tr>";
}

$sth=Null;
$dbh = null;

?>
