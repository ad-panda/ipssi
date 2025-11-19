<?php

require_once "config.php";

$sort = "nom";
if(isset($_GET["sort"])) {
  $sort = $_GET["sort"];
}

$order = "desc";
if(isset($_GET["order"])) {
  $order = $_GET["order"];
}

if(!in_array($sort, ["nom","pays","course","temps"])) {
  die("Invalid sort");
}

if(!in_array($order, ["asc","desc"])) {
  die("Invalid order");
}

$sth = $dbh -> prepare ("SELECT * FROM jo.`100` order by ".$sort." ".$order);
$sth->execute();

$data = $sth->fetchAll(PDO::FETCH_ASSOC);

$url = "href='http://localhost/test/mysql/6.1/test.php?";

echo"<table>
<thead>
<tr>
<th>Nom <a style='" . ($sort == 'nom' && $order == 'asc' ? 'color:red' : '') . " ' href='./test.php?sort=nom&order=asc'>↑</a> <a style=' " . ($sort == 'nom' && $order == 'desc' ? 'color:red' : '') . " ' href='./test.php?sort=nom&order=desc'>↓</a></th>
<th>Pays <a style=' " . ($sort == 'pays' && $order == 'asc' ? 'color:red' : '') . " ' href='./test.php?sort=pays&order=asc'>↑</a> <a style=' " . ($sort == 'pays' && $order == 'desc' ? 'color:red' : '') . " ' href='./test.php?sort=pays&order=desc'>↓</a></th>
<th>Course <a style=' " . ($sort == 'course' && $order == 'asc' ? 'color:red' : '') . " ' href='./test.php?sort=course&order=asc'>↑</a> <a style=' " . ($sort == 'course' && $order == 'desc' ? 'color:red' : '') . " ' href='./test.php?sort=course&order=desc'>↓</a></th> 
<th>Temps <a style=' " . ($sort == 'temps' && $order == 'asc' ? 'color:red' : '') . " ' href='./test.php?sort=temps&order=asc'>↑</a> <a style=' " . ($sort == 'temps' && $order == 'desc' ? 'color:red' : '') . " ' href='./test.php?sort=temps&order=desc'>↓</a></th>
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
