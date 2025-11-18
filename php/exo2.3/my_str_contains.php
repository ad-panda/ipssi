<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>str_contains</title>
</head>
<body>

<form method="post">
    <label for="mot">Entrez un mot :</label>
    <input type="text" id="mot" name="mot" placeholder="Ex : bonjour" required>
    <br><br>
    <label for="mot2">Entrez un mot :</label>
    <input type="text" id="mot2" name="mot2" placeholder="Ex : bonjourmongars" required>
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

    for ($i = 0; $i < $lenH; $i++) {
        for ($j = 0; $j < $lenN; $j++) {
            if (!isset($haystack[$i + $j])) {
                return false; 
            }
            if ($haystack[$i + $j] !== $needle[$j]) {
                break;
            }
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

    if($resultat){
        echo "<strong>$mot</strong> est présent dans $mot2</p>";
    } else {
        echo "<strong>$mot</strong> n'est pas présent dans $mot2</p>";
    }
}
?>

</body>
</html>
