<?php

function carnet()
{
    $fichier = fopen("contact.txt","r");

    $contact = ["Alice Dupont","John Doe","Jean Martin"];

    echo"contact initiaux : <br>";

    foreach($contact as $c){
        echo"<br> $c";
    }



    while (($ligne = fgets($fichier)) !== false) {
        $ligne = trim($ligne);
        if(in_array($ligne,$contact) === false){
            $contact[] = $ligne;
        }
    }

    fclose($fichier);
    echo"<br>";
    foreach($contact as $co){
        echo"<br> $co";
    }
}

carnet();

?>

</body>
</html>
