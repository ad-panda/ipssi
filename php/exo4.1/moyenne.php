
    <?php

    function calcMoy($listeNbr){
      $moy = 0;
      $len = count($listeNbr);

      for ($i = 0; $i < $len; $i++){
        $moy += $listeNbr[$i];
      }

      return ($moy / $len);
    }

    $eleves = [
      ["nom" => "Alice", "notes" =>[15,14,16]],
      ["nom" => "Bob", "notes" =>[12,10,11]],
      ["nom" => "Claire", "notes" =>[18,17,16]]
    ];

    foreach($eleves as $eleve){
        echo "NOM :" . $eleve["nom"] . "<br>";
        echo "notes : " . "<br>";
        foreach ($eleve["notes"] as $note) {
          echo $note . "<br>"; 
        }
        echo "moyenne : " . calcMoy($eleve["notes"]) . "<br>";
    }
      echo "terminer.</p>";
    ?>


