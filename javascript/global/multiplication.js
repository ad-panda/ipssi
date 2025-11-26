
function multiplication(){
    let nb = parseInt(prompt("Donner le nombre de la table ?"));
    let resultat = "la table de multiplication de " + nb + " est : \n\n<br>";
    let i = 1;

    while (i !=  22){
        resultat += "table de " + i + " pour " + nb + " = " + nb*i + " . \n<br>";
        i++;
    }
    let res = document.getElementById("resultattable");
    res.innerHTML = resultat;

    console.log("===calculatrice===");
    console.log(`nombre demander : ${nb} `);
}