function devinette(){
    let nb1 = parseInt(prompt("quelle est le bon nombre sur cette image ?"));

    while (nb1 != 62){
        nb1 = parseInt(prompt("quelle est le bon nombre sur cette image ?"));
    }


    let res = document.getElementById("resultatdevinette");
    res.innerHTML = `<div>Le resultat est bon !!!</div>`;

    console.log("===devinette===");
    console.log(`nombre 1 : ${nb1} `);
}