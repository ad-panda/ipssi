import random
from dataclasses import dataclass, field

# --- Données de base ---
TYPE_CHART = {
    ("Feu", "Plante"): 2.0,
    ("Feu", "Eau"): 0.5,
    ("Eau", "Feu"): 2.0,
    ("Eau", "Plante"): 0.5,
    ("Plante", "Eau"): 2.0,
    ("Plante", "Feu"): 0.5,
}
# Par défaut: 1.0 si combinaison non listée

@dataclass
class Move:
    nom: str
    puissance: int
    type: str
    precision: int = 100  # en %
    pp: int = 10          # points de pouvoir (facultatif)
    pp_max: int = 10

    def utilisable(self) -> bool:
        return self.pp > 0

@dataclass
class Pokemon:
    nom: str
    type: str
    pv_max: int
    attaque: int
    defense: int
    vitesse: int
    moves: list[Move] = field(default_factory=list)
    pv: int = None

    def __post_init__(self):
        if self.pv is None:
            self.pv = self.pv_max

    def vivant(self) -> bool:
        return self.pv > 0

    def choisir_move_ia(self):
        utilisables = [m for m in self.moves if m.utilisable()]
        if not utilisables:
            return None
        # petite préférence pour les moves de type avantageux
        random.shuffle(utilisables)
        utilisables.sort(key=lambda m: random.random() + avantage_type(m.type, None), reverse=True)
        return utilisables[0]

# --- Mécaniques ---
def avantage_type(type_attaque: str, type_defense: str | None) -> float:
    if type_defense is None:
        return 0.0
    return TYPE_CHART.get((type_attaque, type_defense), 1.0)

def calcul_degats(attaquant: Pokemon, cible: Pokemon, move: Move) -> int:
    if random.randint(1,100) > move.precision:
        return -1  # -1 => miss
    stab = 1.5 if move.type == attaquant.type else 1.0
    eff = avantage_type(move.type, cible.type)
    # Formule simplifiée
    base = (((2 * 50 / 5) + 2) * move.puissance * (attaquant.attaque / max(1, cible.defense)) / 50) + 2
    deg = int(base * stab * eff * random.uniform(0.85, 1.0))
    return max(1, deg)

def barre_pv(pv, pv_max, largeur=20):
    ratio = max(0, pv) / pv_max
    verts = int(ratio * largeur)
    return "[" + "#" * verts + "-" * (largeur - verts) + f"] {pv}/{pv_max}"

def prompt_entier(texte, mini, maxi):
    while True:
        try:
            n = int(input(texte))
            if mini <= n <= maxi:
                return n
        except ValueError:
            pass
        print(f"→ Entre un nombre entre {mini} et {maxi}.")

# --- Création de quelques Pokémon ---
def starter_pack():
    feu = Pokemon(
        nom="Pyralion", type="Feu", pv_max=80, attaque=18, defense=10, vitesse=14,
        moves=[
            Move("Flammèche", 40, "Feu", 100, 25, 25),
            Move("Griffe", 40, "Normal", 100, 35, 35),
            Move("Rugissement", 0, "Normal", 100, 30, 30),
        ],
    )
    eau = Pokemon(
        nom="Aquafleau", type="Eau", pv_max=85, attaque=16, defense=12, vitesse=12,
        moves=[
            Move("Pistolet à O", 40, "Eau", 100, 25, 25),
            Move("Charge", 40, "Normal", 100, 35, 35),
            Move("Bulle", 40, "Eau", 100, 30, 30),
        ],
    )
    plante = Pokemon(
        nom="Foliar", type="Plante", pv_max=90, attaque=15, defense=14, vitesse=10,
        moves=[
            Move("Fouet Lianes", 45, "Plante", 100, 25, 25),
            Move("Charge", 40, "Normal", 100, 35, 35),
            Move("Tranch'Herbe", 55, "Plante", 95, 25, 25),
        ],
    )
    return feu, eau, plante

def reset_pp(poke: Pokemon):
    for m in poke.moves:
        m.pp = m.pp_max

# --- Combat ---
def tour(attaquant: Pokemon, defenseur: Pokemon, is_player: bool):
    print(f"\n👉 {attaquant.nom} attaque !")
    if is_player:
        # afficher moves
        dispo = [m for m in attaquant.moves if m.utilisable()]
        if not dispo:
            print("Plus de PP !", attaquant.nom, "passe son tour…")
            return
        print("Choisis une attaque :")
        for i, m in enumerate(attaquant.moves, 1):
            info = f"{m.nom} ({m.type}) Pow:{m.puissance} PP:{m.pp}/{m.pp_max}"
            print(f"  {i}. {info}")
        choix = prompt_entier("> ", 1, len(attaquant.moves))
        move = attaquant.moves[choix-1]
        if not move.utilisable():
            print("Cette attaque n'a plus de PP ! Tour perdu.")
            return
    else:
        move = attaquant.choisir_move_ia()
        if move is None:
            print(f"{attaquant.nom} n'a plus de PP et passe son tour.")
            return
        print(f"L'adversaire utilise {move.nom} !")

    move.pp -= 1
    deg = calcul_degats(attaquant, defenseur, move)
    if deg == -1:
        print(f"{attaquant.nom} utilise {move.nom}… mais rate !")
        return
    eff = avantage_type(move.type, defenseur.type)
    defenseur.pv -= deg
    eff_txt = ""
    if eff > 1.0:
        eff_txt = " C'est super efficace !"
    elif eff < 1.0:
        eff_txt = " Ce n'est pas très efficace…"
    print(f"{move.nom} inflige {deg} dégâts.{eff_txt}")
    print(f"{defenseur.nom} {barre_pv(defenseur.pv, defenseur.pv_max)}")

def combat(player: Pokemon, ennemi: Pokemon):
    reset_pp(player); reset_pp(ennemi)
    sac = {"Potion": 2}  # +20 PV
    print("\n=== COMBAT ===")
    print(f"Tu envoies {player.nom} ({player.type}) !")
    print(f"L'adversaire envoie {ennemi.nom} ({ennemi.type}) !")

    while player.vivant() and ennemi.vivant():
        print("\n--- Ton tour ---")
        print(f"1. Attaquer  2. Sac (Potion x{sac['Potion']})  3. Fuir")
        action = prompt_entier("> ", 1, 3)
        if action == 2:
            if sac["Potion"] > 0:
                soin = 20
                pv_av = player.pv
                player.pv = min(player.pv_max, player.pv + soin)
                sac["Potion"] -= 1
                print(f"Tu utilises une Potion (+{player.pv - pv_av} PV). {player.nom} {barre_pv(player.pv, player.pv_max)}")
            else:
                print("Plus de potions !")
        elif action == 3:
            if random.random() < 0.5:
                print("Tu t'échappes avec succès !")
                return
            else:
                print("Impossible de fuir !")
        else:
            # Attaque du joueur
            tour(player, ennemi, is_player=True)
        if not ennemi.vivant():
            break

        # Tour de l'ennemi
        print("\n--- Tour adverse ---")
        if random.random() < 0.1 and ennemi.pv <= ennemi.pv_max - 20:
            # l'ennemi a 10% de chance d'utiliser une "potion" si blessé
            soin = 20
            ennemi.pv = min(ennemi.pv_max, ennemi.pv + soin)
            print(f"L'adversaire utilise une potion. {ennemi.nom} {barre_pv(ennemi.pv, ennemi.pv_max)}")
        else:
            tour(ennemi, player, is_player=False)

    # Fin du combat
    if player.vivant() and not ennemi.vivant():
        print(f"\n🎉 {ennemi.nom} est K.O. ! Tu gagnes le combat !")
    elif ennemi.vivant() and not player.vivant():
        print(f"\n💀 {player.nom} est K.O. ! Tu perds le combat…")
    else:
        print("\nLe combat est interrompu.")

def choisir_starter():
    starters = starter_pack()
    noms = [p.nom for p in starters]
    print("Choisis ton starter :")
    for i, p in enumerate(starters, 1):
        print(f"  {i}. {p.nom} ({p.type})  PV:{p.pv_max} Atk:{p.attaque} Def:{p.defense} Vit:{p.vitesse}")
    i = prompt_entier("> ", 1, len(starters))
    joueur = starters[i-1]
    # ennemi d'un type aléatoire
    adversaires = [p for j, p in enumerate(starters) if j != (i-1)]
    ennemi = random.choice(adversaires)
    # cloner pour ne pas partager l'état
    import copy
    return copy.deepcopy(joueur), copy.deepcopy(ennemi)

def main():
    print("=== Mini Pokémon (console) ===")
    while True:
        joueur, ennemi = choisir_starter()
        combat(joueur, ennemi)
        # Rejouer ?
        print("\nRejouer ? 1=Oui  2=Non")
        if prompt_entier("> ", 1, 2) == 2:
            print("Merci d'avoir joué !")
            break

if __name__ == "__main__":
    main()
