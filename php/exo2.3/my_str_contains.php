<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>str_contains</title>
</head>
<body>

<form method="post">
    <label for="mot">Entrez un mot :</label>
    <input type="text" id="mot" name="mot" placeholder="Ex :bonjour monsieurrr (haystack)" required>
    <br><br>
    <label for="mot2">Entrez un mot :</label>
    <input type="text" id="mot2" name="mot2" placeholder="Ex : bonjour (needle)" required>
    <br><br>
    <button type="submit">Envoyer</button>
</form>

<?php

function my_str_contains($haystack, $needle)
{
    $lenH = count($haystack);
    $lenN = count($needle);

    if ($lenN > $lenH) {
        return false;
    }

    for ($i = 0; $i <= $lenH - $lenN; $i++) {
        $j = 0;
        while ($j < $lenN && isset($haystack[$i + $j]) && $haystack[$i + $j] === $needle[$j]) {
            $j++;
        }
        if ($j === $lenN) {
            return true;
        }
    }

    return false;
}


if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $mot = $_POST["mot"];
    $mot2 = $_POST["mot2"];

    $tab = str_split($mot);
    $tab2 = str_split($mot2);

    $resultat = my_str_contains($tab, $tab2);

    echo "<p>Mot original : $mot et $mot2<br>";

    if($resultat === TRUE){
        echo "<strong>$mot2</strong> est présent dans $mot</p>";
    } else {
        echo "<strong>$mot2</strong> n'est pas présent dans $mot</p>";
    }
}
?>

</body>
</html>
