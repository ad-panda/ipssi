Projet Php :

Groupe :

- Adrien Simoes Ferreira
- Maxim Nocella


Index.php

- charge les fonctions

- récupère les données envoyées par le formulaire

- appelle la fonction translate()

- prépare les variables pour l’affichage

- passe tout au template (PHTML)


template.phtml

- Afficher le formulaire si aucune traduction n’a encore été faite.

- Afficher un message d’erreur si le contrôleur a détecté un problème.

- Afficher le résultat de la traduction si le mot existe dans le dictionnaire.

- Afficher la liste des mots connus si le mot est introuvable.

- Permettre de refaire une traduction en revenant au formulaire.


Translate.php

- cette page sert de bibliothèque de fonctions et centre logique du traducteur.