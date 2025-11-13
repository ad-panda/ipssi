<?php

// Permet d'eviter des erreurs d'information renvoyer
$nom = htmlspecialchars(trim($_POST['nom'] ?? ''));
$email = htmlspecialchars(trim($_POST['email'] ?? ''));
$password = htmlspecialchars(trim($_POST['password'] ?? ''));
$sexe = htmlspecialchars($_POST['sexe'] ?? '');
$ville = htmlspecialchars($_POST['ville'] ?? '');
$loisirs = $_POST['loisirs'] ?? [];
$animaux = $_POST['animaux'] ?? [];

// conditions pour valider le remplissage du formulaire ou le faire reremplir
$erreurs = [];

if (strlen($nom) < 2 || strlen($nom) > 50) {
    $erreurs[] = "Le nom doit contenir entre 2 et 50 caractères.";
}

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    $erreurs[] = "L'email n'est pas valide.";
}

if (strlen($password) < 6) {
    $erreurs[] = "Le mot de passe doit contenir au moins 6 caractères.";
}

if (!in_array($sexe, ['H', 'F'])) {
    $erreurs[] = "Le sexe doit être H ou F.";
}

$villesAutorisees = ["Paris", "Lyon", "Marseille", "Toulouse"];
if (!in_array($ville, $villesAutorisees)) {
    $erreurs[] = "Ville non reconnue.";
}

// 
if (!empty($erreurs)) {
    echo "<h2>Erreurs détectées :</h2><ul>";
    foreach ($erreurs as $e) {
        echo "<li>$e</li>";
    }
    echo "</ul><a href='index.html'>← Retour au formulaire</a>";
    exit;
}

// fausse liste
$profils = [
    ["nom" => "Alice", "ville" => "Paris", "sexe" => "F", "loisirs" => ["Lecture", "Musique"]],
    ["nom" => "Bob", "ville" => "Lyon", "sexe" => "H", "loisirs" => ["Sport"]],
    ["nom" => "Claire", "ville" => "Marseille", "sexe" => "F", "loisirs" => ["Musique", "Sport"]],
    ["nom" => "David", "ville" => "Toulouse", "sexe" => "H", "loisirs" => ["Lecture"]],
];

// Filtrage des profils qui partagent la même ville ou un loisir
$resultats = array_filter($profils, function($p) use ($ville, $loisirs) {
    return $p['ville'] === $ville || count(array_intersect($p['loisirs'], $loisirs)) > 0;
});
?>

<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Résultat du formulaire</title>
</head>
<body>
  <h2>Récapitulatif des informations</h2>
  <ul>
    <li><strong>Nom :</strong> <?= $nom ?></li>
    <li><strong>Email :</strong> <?= $email ?></li>
    <li><strong>Sexe :</strong> <?= $sexe === 'H' ? 'Homme' : 'Femme' ?></li>
    <li><strong>Ville :</strong> <?= $ville ?></li>
    <li><strong>Loisirs :</strong> <?= implode(', ', $loisirs) ?: 'Aucun' ?></li>
    <li><strong>Animaux :</strong> <?= implode(', ', $animaux) ?: 'Aucun' ?></li>
  </ul>

  <h2>Profils similaires trouvés :</h2>
  <?php if (empty($resultats)): ?>
    <p>Aucun profil correspondant.</p>
  <?php else: ?>
    <ul>
      <?php foreach ($resultats as $profil): ?>
        <li><?= $profil['nom'] ?> — <?= $profil['ville'] ?> (<?= $profil['sexe'] ?>)</li>
      <?php endforeach; ?>
    </ul>
  <?php endif; ?>

  <a href="index.html">← Retour au formulaire</a>
</body>
</html>
