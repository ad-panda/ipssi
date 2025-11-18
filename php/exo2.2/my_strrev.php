<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Reverse String</title>
</head>
<body>

<form method="post">
    <label for="mot">Entrez un mot :</label>
    <input type="text" id="mot" name="mot" placeholder="Ex : bonjour" required>
    <br><br>
    <button type="submit">Envoyer</button>
</form>

<?php


function my_strrev($tab)
{
    $len = count($tab);
    $rev = [];

    for ($i = 0; $i < $len; $i++) {

        $indexInverse = $len - 1 - $i;

        $rev[$i] = $tab[$indexInverse];
    }

    return $rev;
}

if ($_SERVER["REQUEST_METHOD"] === "POST") {

    $mot = $_POST["mot"];

    // Convertir le mot en tableau de lettres
    $tab = str_split($mot);

    $tabInverse = my_strrev($tab);

    // Reconstruire le mot inversé
    $motInverse = implode("", $tabInverse);

    echo "<p>Mot original : $mot<br>";
    echo "Mot inversé : <strong>$motInverse</strong></p>";
}
?>

</body>
</html>
