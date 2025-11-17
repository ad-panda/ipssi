<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Formulaire Prénom</title>
</head>
<body>
    <h2>Veuillez entrer votre prénom</h2>

    <form method="post">
        <label for="age">Age :</label>
        <input type="text" id="age" name="age" required>
        <br><br>
        <button type="submit">Envoyer</button>
    </form>
    <?php
    function structure($age){
      if ($age <= 3)
        echo"a la creche";
        else if ($age <= 6)
          echo"a la maternelle";
          else if ($age <= 11)
          echo"a l'ecole primaire";
          else if ($age <= 16)
          echo"au college";
          else if ($age <= 18)
          echo "au lycee";
          else 
          echo "en etude sup";
    } 

      $age = (int)($_POST["age"]);
      echo "<p>Pour $age ans, vous êtes " ;
      structure($age);
      echo ".</p>";
    ?>
</body>
</html>

