<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>doubleboucle</title>
</head>
<body>
    <?php
    function doubleboucle($nbr){
      $i = 0;
      $liste = "";

      while ($i != $nbr){
        $i = $i + 1;
        $j = 0;
        while($j != $i){
          $j = $j + 1;
          $liste .= "$i";
        }
        $liste .= "<br>";
      }
      return $liste;
    } 

      $nbr = 5;
      $liste=doubleboucle($nbr);
      echo "<p>affiche pour $nbr <br>" ;
      echo"$liste<br>";
      echo "terminer.</p>";
    ?>
</body>
</html>

