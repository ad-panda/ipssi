<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>doubleboucle</title>
</head>
<body>
<form method="post">
        <label for="nbr">Entrez des nombres séparés par des virgules :</label>
        <input type="text" id="nbr" name="nbr" placeholder="Ex : 10,20,30" required>
        <br><br>
        <button type="submit">Envoyer</button>
    </form>
    <?php

    function calcMoy($listeNbr){
      $moy = 0;
      $len = count($listeNbr);

      for ($i = 0; $i != $len; $i++){
        $moy += $listeNbr[$i];
      }

      return ($moy / $len);
    }

    $liste = ($_POST["nbr"]);

    $listeBrute = explode(",",$liste);

    $listeNbr = array_map("intval", $listeBrute);

    $moyenne = calcMoy($listeNbr);

    $listeAffichage = implode(",",$listeNbr);

      echo "<p>affiche pour cette liste $listeAffichage la moyenne qui est de :<br>" ;
      echo"$moyenne<br>";
      echo "terminer.</p>";
    ?>
</body>
</html>

