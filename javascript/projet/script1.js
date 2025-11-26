tour = "a";

const image1 = "x.png";
const image2 = "o.png"



function aba() {

    if (tour == "a")
        tour = "b";
    else
        tour = "a";

};

function ecr(btn) {
    let bouton = document.getElementById(btn);
    if (tour == "a")
        bouton.innerHTML = `<img src="o.png" width="140" heigth="140">`;
    else
        bouton.innerHTML = `<img src="x.png" width="140" heigth="140">`;
    


};

function verif(idBouton) {
    let bouton = document.getElementById(idBouton);
    let img = bouton.querySelector('img');

    // On compare directement le src relatif
    if (img.getAttribute('src') === image1) {
        prompt("✅ l'image de X");
    } else if (img.getAttribute('src') === image2){
        prompt("l'image de O");
    }
};