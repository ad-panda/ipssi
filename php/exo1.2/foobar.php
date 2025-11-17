<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Formulaire Prénom</title>
</head>
<body>
    <?php
    function foobar(){
      $i = 0;
      $liste = "";

      while ($i != 100){
        $i = $i + 1;
        if ($i % 3 == 0 && $i % 5 == 0)
          $liste .= "foobar <br>";
        else if ($i % 5 == 0)
          $liste .= "bar <br>";
        else if ($i % 3 == 0)
          $liste .= "foo <br>";
        else 
          $liste .= "$i <br>";
      }
      return $liste;
    } 

      $liste=foobar();
      echo "<p>affiche de 1 a 100 <br>" ;
      echo"$liste";
      echo "terminer.</p>";
    ?>
</body>
</html>

