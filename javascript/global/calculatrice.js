
function calculatrice(){
    let nb1 = parseInt(prompt("le premier nombre ?"));
    let operation = String(prompt("quelle operation voulez vous faire (+,-,*,/)?"));
    let nb2 = parseInt(prompt("le deuxieme nombre ?"));
    let op = 0;


    if (operation == "+"){
        op = nb1 + nb2;
    } else if (operation == "-"){
        op = nb1 - nb2;
    } else if (operation == "*"){
        op = nb1 * nb2;
    } else if (operation == "/"){
        op = nb1 / nb2;
    }

    let res = document.getElementById("resultatcalculatrice");
    res.innerHTML = `<div>Le resultat est : ${op} </div>`;

    console.log("===calculatrice===");
    console.log(`nombre 1 : ${nb1} `);
    console.log(`nombre 1 : ${nb2} `);
}