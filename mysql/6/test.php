<?php

session_start();

$_SESSION["email"] = "john@gmail.com";

if (!isset($_SESSION["counter"]))
{
  $_SESSION["counter"] = 0;
}

$_SESSION["counter"]++;

require_once "config.php";

//creer variable et verifie si variable definie par l'url a l'ouverture du fichier et donne la bonne valeur a la variable

$sort = "nom";

if (isset($_GET["sort"])) {
  $sort = $_GET["sort"];
}

$order = "asc";

if (isset($_GET["order"])) {
 $order = $_GET["order"];
}

//permet de verifier que l'url correspond a des variables existant dans le mysql

if(!in_array($sort, ["nom","pays","course","temps"])) {
  die("Invalid sort");
}

if(!in_array($order, ["asc","desc"])) {
  die("Invalid order");
}

//verification method et si username existe deja


if ($_SERVER["REQUEST_METHOD"] === "POST") {
  $_SESSION["username"] = $_POST["username"];
}


if (isset($_SESSION["username"]))
{
  echo '
  <h1>l\'utilisateur '.$_SESSION["username"].' est connecter</h1>
  ';
} else {
  echo '
  <form action="test.php" method="POST">
<h1>Login</h1>
<label>Username : </label>
<input type="text" id="username" name="username">
</form>
  ';
}


$sth=$dbh->prepare("SELECT * FROM jo.`100` order by ".$sort." ".$order);
$sth->execute();

$data = $sth->fetchAll(PDO::FETCH_ASSOC);

echo "<h1>".$_SESSION["counter"]."</h1>";

echo"<table>
<thead>
<tr>
<th>
Nom 
<a style='" . ($sort == 'nom' && $order == 'asc' ? 'color:red' : '') . " ' href='./test.php?sort=nom&order=asc'>↑</a> 
<a style=' " . ($sort == 'nom' && $order == 'desc' ? 'color:red' : '') . " ' href='./test.php?sort=nom&order=desc'>↓</a>
</th>
<th>
Pays 
<a style=' " . ($sort == 'pays' && $order == 'asc' ? 'color:red' : '') . " ' href='./test.php?sort=pays&order=asc'>↑</a> 
<a style=' " . ($sort == 'pays' && $order == 'desc' ? 'color:red' : '') . " ' href='./test.php?sort=pays&order=desc'>↓</a>
</th>
<th>
Course 
<a style=' " . ($sort == 'course' && $order == 'asc' ? 'color:red' : '') . " ' href='./test.php?sort=course&order=asc'>↑</a> 
<a style=' " . ($sort == 'course' && $order == 'desc' ? 'color:red' : '') . " ' href='./test.php?sort=course&order=desc'>↓</a>
</th> 
<th>
Temps 
<a style=' " . ($sort == 'temps' && $order == 'asc' ? 'color:red' : '') . " ' href='./test.php?sort=temps&order=asc'>↑</a> 
<a style=' " . ($sort == 'temps' && $order == 'desc' ? 'color:red' : '') . " ' href='./test.php?sort=temps&order=desc'>↓</a>
</th>
</tr>
</thead>";
foreach($data as $value){
  echo "<tr>
  <td>".$value["nom"]."</td>
  <td>".$value["pays"]."</td>
  <td>".$value["course"]."</td>
  <td>".$value["temps"]."</td>
  </tr>";
}

$sth=Null;
$dbh = null;
?>
