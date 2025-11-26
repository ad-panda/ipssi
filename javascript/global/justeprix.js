

function justeprix(){
    let nb = parseInt(prompt("quelle est le bon nombre entre 1 et 100 ?"));
    let i = 0;

    while (nb != 60 && i < 7){
        if (i == 4){
            nb = parseInt(prompt("Vous etes a votre 4 eme essai sur 7 ! quelle est le bon nombre entre 1 et 100 ?"));
        } else {
            nb = parseInt(prompt("quelle est le bon nombre entre 1 et 100 ?"));
        }
        i++;
    }

    if (i == 7){
        let res = document.getElementById("resultatjusteprix");
        res.innerHTML = `<div>Tu as perdu!!!</div>`;
    } else {
        let res = document.getElementById("resultatjusteprix");
        res.innerHTML = `<div>Tu as trouver le bon prix !!!</div>`;
    }

    console.log("===juste prix===");
    console.log(`nombre demander : ${nb} `);
}