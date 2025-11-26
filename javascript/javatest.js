

            const a = "../calculette.jpeg"; // chemin de référence
            const b = "../table.jpeg";      // autre image
        
            function verif(idBouton) {
                let bouton = document.getElementById(idBouton);
                let img = bouton.querySelector('img'); // récupère l'image dans le bouton
        
                // Vérifie si l'image correspond à 'a'
                if (img.src.endsWith(b)) {
                    prompt("bonjour");
                } else {
                    prompt("sheeesh");
                }
            }


        <script>
            let boite = document.getElementById("cercle");

            boite.addEventListener("mouseover", function() {
                boite.style.background = "red";
                boite.style.transform = "scale(1.2)";
            }
            );

            boite.addEventListener("mouseout", function() {
                boite.style.background = "white";
                boite.style.transform = "scale(1)";
            }
            );

        </script>