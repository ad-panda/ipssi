<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>doubleboucle</title>
</head>
<body>
<form method="post">
        <label for="nbr">nombre :</label>
        <input type="int" id="nbr" name="nbr" required>
        <br><br>
        <button type="submit">Envoyer</button>
    </form>
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

      $nbr = (int)($_POST["nbr"]);
      $liste=doubleboucle($nbr);
      echo "<p>affiche pour $nbr <br>" ;
      echo"$liste<br>";
      echo "terminer.</p>";
    ?>
</body>
</html>

