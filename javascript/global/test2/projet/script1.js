let tour = "X"; 
let joueur1 = "";
let joueur2 = "";

function commencerJeu() {
    const inputJ1 = document.getElementById("joueur1").value.trim();
    const inputJ2 = document.getElementById("joueur2").value.trim();


    if (inputJ1.length < 1 || inputJ2.length < 1) {
        alert("Veuillez saisir le nom des deux joueurs pour commencer la partie !");
        return; 
    }

    joueur1 = inputJ1;
    joueur2 = inputJ2;

    // pour le premier joueur qui commence

    document.getElementById("tourActuel").textContent = `C'est à ${joueur1} (X) de jouer !`;

    // supprime les formulaires du site web quand le jeux commence

    document.getElementById("joueursForm").style.display = "none";

    // permet de rendre les different bouton du tableau cliquable

    document.getElementById("tabl").style.pointerEvents = "auto";
}


function jouer(id) {
    const bouton = document.getElementById(id);

    // Empêche de rejouer sur un bouton déjà remplis

    if (bouton.querySelector("img")) return;

    // Permet d'inserer les bons symboles

    const couleur = tour === "X" ? "red" : "dodgerblue";
    const symbole = tour === "X" ? "x" : "o";

    bouton.innerHTML = `<img src="${symbole}.png" alt="${tour}" style="filter: drop-shadow(0 0 8px ${couleur});">`;

    // permet l'animation du zoom  sur les symboles

    const img = bouton.querySelector("img");
    img.classList.add("zoom");
    setTimeout(() => img.classList.remove("zoom"), 300);

    // Vérifie la victoire
    const combinaison = verifVictoire();
    if (combinaison) {
        const gagnant = tour === "X" ? joueur1 : joueur2;
        document.getElementById("resultatJeu").textContent = `🎉 ${gagnant} a gagné !`;
        surlignerVictoire(combinaison);
        afficherOverlayVictoire(gagnant);
        return;
    }

    // verifie si le Match est nul 
    if (estMatchNul()) {
        document.getElementById("resultatJeu").textContent = "😐 Match nul !";
        afficherOverlayVictoire("Match nul !");
        return;
    }

    // Changement du joueur
    tour = tour === "X" ? "O" : "X";
    const prochain = tour === "X" ? joueur1 : joueur2;
    document.getElementById("tourActuel").textContent = `C'est à ${prochain} (${tour}) de jouer !`;
}

function verifVictoire() {
    const combinaisons = [
        ["btn1", "btn2", "btn3"],
        ["btn4", "btn5", "btn6"],
        ["btn7", "btn8", "btn9"],
        ["btn1", "btn4", "btn7"],
        ["btn2", "btn5", "btn8"],
        ["btn3", "btn6", "btn9"],
        ["btn1", "btn5", "btn9"],
        ["btn3", "btn5", "btn7"]
    ];

    for (let combo of combinaisons) {
        const [a, b, c] = combo.map(id => document.getElementById(id).querySelector("img")?.getAttribute("src"));
        if (a && a === b && a === c) return combo;
    }
    return null;
}

function estMatchNul() {
    for (let i = 1; i <= 9; i++) {
        if (!document.getElementById(`btn${i}`).querySelector("img")) return false;
    }
    return true;
}

function reinitialiser() {
    for (let i = 1; i <= 9; i++) {
        const bouton = document.getElementById(`btn${i}`);
        bouton.innerHTML = "";
        bouton.disabled = false;
    }
    document.getElementById("resultatJeu").textContent = "";
    const overlay = document.getElementById("overlayVictoire");
    overlay.style.display = "none";
    overlay.style.pointerEvents = "none"; // ne bloque pas les clics
    tour = "X";
    document.getElementById("tourActuel").textContent = `C'est à ${joueur1} (X) de jouer !`;
}

function surlignerVictoire(combo) {
    combo.forEach(id => {
        const img = document.getElementById(id).querySelector("img");
        if (img) img.classList.add("victoire");
    });
}

function afficherOverlayVictoire(gagnant) {
    const overlay = document.getElementById("overlayVictoire");
    const texte = document.getElementById("texteVictoire");
    texte.textContent = `🏆 ${gagnant} a gagné !`;
    overlay.style.display = "flex";
    overlay.style.pointerEvents = "none"; // L’animation est visible mais ne bloque pas les clics
}
