import curses
import random

def choisir_difficulte():
    print("=== SNAKE GAME ===")
    print("Choisis la difficulté :")
    print("1. Facile")
    print("2. Normal")
    print("3. Difficile")
    choix = input("👉 Entrez 1, 2 ou 3 : ")
    
    if choix == "1":
        return 200   # plus lent
    elif choix == "3":
        return 80    # plus rapide
    else:
        return 120   # valeur par défaut (normal)

def main(stdscr, vitesse):
    # Configuration de base
    curses.curs_set(0)            # cacher le curseur
    sh, sw = stdscr.getmaxyx()    # hauteur et largeur de l'écran
    win = curses.newwin(sh, sw, 0, 0)
    win.keypad(1)
    win.timeout(vitesse)          # vitesse selon choix

    # Position initiale du serpent
    snk_x = sw // 4
    snk_y = sh // 2
    snake = [
        (snk_y, snk_x),
        (snk_y, snk_x - 1),
        (snk_y, snk_x - 2)
    ]

    # Première nourriture
    food = (sh // 2, sw // 2)
    win.addch(food[0], food[1], "🍎")

    # Direction initiale
    key = curses.KEY_RIGHT
    score = 0

    while True:
        win.border(0)
        win.addstr(0, 2, f" Score : {score} ")
        win.addstr(0, sw // 2 - 6, " SNAKE GAME ")

        # Lecture touche
        next_key = win.getch()
        key = key if next_key == -1 else next_key

        # Calcul nouvelle tête
        y, x = snake[0]
        if key == curses.KEY_DOWN:
            y += 1
        elif key == curses.KEY_UP:
            y -= 1
        elif key == curses.KEY_LEFT:
            x -= 1
        elif key == curses.KEY_RIGHT:
            x += 1
        new_head = (y, x)

        # Conditions de fin
        if (
            y == 0 or y == sh-1 or
            x == 0 or x == sw-1 or
            new_head in snake
        ):
            msg = f" GAME OVER ! Score final : {score} "
            win.addstr(sh // 2, sw // 2 - len(msg)//2, msg)
            win.nodelay(0)
            win.getch()
            break

        # Ajout nouvelle tête
        snake.insert(0, new_head)

        # Si la pomme est mangée
        if snake[0] == food:
            score += 1
            food = None
            while food is None:
                nf = (
                    random.randint(1, sh-2),
                    random.randint(1, sw-2)
                )
                if nf not in snake:
                    food = nf
            win.addch(food[0], food[1], "🍎")
        else:
            # enlève la queue
            tail = snake.pop()
            win.addch(tail[0], tail[1], " ")

        # Dessiner la tête du serpent
        win.addch(snake[0][0], snake[0][1], "■")

if __name__ == "__main__":
    vitesse = choisir_difficulte()
    curses.wrapper(main, vitesse)
