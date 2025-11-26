
def fct_puissance4():
    
    a6=" "; a1=" "; a2=" "; a3=" "; a4=" "; a5=" "
    b6=" "; b1=" "; b2=" "; b3=" "; b4=" "; b5=" "
    c6=" "; c1=" "; c2=" "; c3=" "; c4=" "; c5=" "
    d6=" "; d1=" "; d2=" "; d3=" "; d4=" "; d5=" "
    e6=" "; e1=" "; e2=" "; e3=" "; e4=" "; e5=" "
    f6=" "; f1=" "; f2=" "; f3=" "; f4=" "; f5=" "
    g6=" "; g1=" "; g2=" "; g3=" "; g4=" "; g5=" "
    
    t = 0

    colonne = str
    

    # boucle while avec comme conditions tant que aucune position gagnante n'est trouver et
    # tant que que tous les emplacements ne sont pas vide 

    while a1+b1+c1+d1 != "XXXX" and a1+b1+c1+d1 != "OOOO" \
    and b1+c1+d1+e1 != "XXXX" and b1+c1+d1+e1 != "OOOO" \
    and c1+d1+e1+f1 != "XXXX" and c1+d1+e1+f1 != "OOOO" \
    and d1+e1+f1+g1 != "XXXX" and d1+e1+f1+g1 != "OOOO" \
    and a2+b2+c2+d2 != "XXXX" and a2+b2+c2+d2 != "OOOO" \
    and b2+c2+d2+e2 != "XXXX" and b2+c2+d2+e2 != "OOOO" \
    and c2+d2+e2+f2 != "XXXX" and c2+d2+e2+f2 != "OOOO" \
    and d2+e2+f2+g2 != "XXXX" and d2+e2+f2+g2 != "OOOO" \
    and a3+b3+c3+d3 != "XXXX" and a3+b3+c3+d3 != "OOOO" \
    and b3+c3+d3+e3 != "XXXX" and b3+c3+d3+e3 != "OOOO" \
    and c3+d3+e3+f3 != "XXXX" and c3+d3+e3+f3 != "OOOO" \
    and d3+e3+f3+g3 != "XXXX" and d3+e3+f3+g3 != "OOOO" \
    and a4+b4+c4+d4 != "XXXX" and a4+b4+c4+d4 != "OOOO" \
    and b4+c4+d4+e4 != "XXXX" and b4+c4+d4+e4 != "OOOO" \
    and c4+d4+e4+f4 != "XXXX" and c4+d4+e4+f4 != "OOOO" \
    and d4+e4+f4+g4 != "XXXX" and d4+e4+f4+g4 != "OOOO" \
    and a5+b5+c5+d5 != "XXXX" and a5+b5+c5+d5 != "OOOO" \
    and b5+c5+d5+e5 != "XXXX" and b5+c5+d5+e5 != "OOOO" \
    and c5+d5+e5+f5 != "XXXX" and c5+d5+e5+f5 != "OOOO" \
    and d5+e5+f5+g5 != "XXXX" and d5+e5+f5+g5 != "OOOO" \
    and a6+b6+c6+d6 != "XXXX" and a6+b6+c6+d6 != "OOOO" \
    and b6+c6+d6+e6 != "XXXX" and b6+c6+d6+e6 != "OOOO" \
    and c6+d6+e6+f6 != "XXXX" and c6+d6+e6+f6 != "OOOO" \
    and d6+e6+f6+g6 != "XXXX" and d6+e6+f6+g6 != "OOOO" \
    and a1+a2+a3+a4 != "XXXX" and a1+a2+a3+a4 != "OOOO" \
    and a2+a3+a4+a5 != "XXXX" and a2+a3+a4+a5 != "OOOO" \
    and a3+a4+a5+a6 != "XXXX" and a3+a4+a5+a6 != "OOOO" \
    and b1+b2+b3+b4 != "XXXX" and b1+b2+b3+b4 != "OOOO" \
    and b2+b3+b4+b5 != "XXXX" and b2+b3+b4+b5 != "OOOO" \
    and b3+b4+b5+b6 != "XXXX" and b3+b4+b5+b6 != "OOOO" \
    and c1+c2+c3+c4 != "XXXX" and c1+c2+c3+c4 != "OOOO" \
    and c2+c3+c4+c5 != "XXXX" and c2+c3+c4+c5 != "OOOO" \
    and c3+c4+c5+c6 != "XXXX" and c3+c4+c5+c6 != "OOOO" \
    and d1+d2+d3+d4 != "XXXX" and d1+d2+d3+d4 != "OOOO" \
    and d2+d3+d4+d5 != "XXXX" and d2+d3+d4+d5 != "OOOO" \
    and d3+d4+d5+d6 != "XXXX" and d3+d4+d5+d6 != "OOOO" \
    and e1+e2+e3+e4 != "XXXX" and e1+e2+e3+e4 != "OOOO" \
    and e2+e3+e4+e5 != "XXXX" and e2+e3+e4+e5 != "OOOO" \
    and e3+e4+e5+e6 != "XXXX" and e3+e4+e5+e6 != "OOOO" \
    and f1+f2+f3+f4 != "XXXX" and f1+f2+f3+f4 != "OOOO" \
    and f2+f3+f4+f5 != "XXXX" and f2+f3+f4+f5 != "OOOO" \
    and f3+f4+f5+f6 != "XXXX" and f3+f4+f5+f6 != "OOOO" \
    and g1+g2+g3+g4 != "XXXX" and g1+g2+g3+g4 != "OOOO" \
    and g2+g3+g4+g5 != "XXXX" and g2+g3+g4+g5 != "OOOO" \
    and g3+g4+g5+g6 != "XXXX" and g3+g4+g5+g6 != "OOOO" \
    and a1+b2+c3+d4 != "XXXX" and a1+b2+c3+d4 != "OOOO" \
    and b1+c2+d3+e4 != "XXXX" and b1+c2+d3+e4 != "OOOO" \
    and c1+d2+e3+f4 != "XXXX" and c1+d2+e3+f4 != "OOOO" \
    and d1+e2+f3+g4 != "XXXX" and d1+e2+f3+g4 != "OOOO" \
    and a2+b3+c4+d5 != "XXXX" and a2+b3+c4+d5 != "OOOO" \
    and b2+c3+d4+e5 != "XXXX" and b2+c3+d4+e5 != "OOOO" \
    and c2+d3+e4+f5 != "XXXX" and c2+d3+e4+f5 != "OOOO" \
    and d2+e3+f4+g5 != "XXXX" and d2+e3+f4+g5 != "OOOO" \
    and a3+b4+c5+d6 != "XXXX" and a3+b4+c5+d6 != "OOOO" \
    and b3+c4+d5+e6 != "XXXX" and b3+c4+d5+e6 != "OOOO" \
    and c3+d4+e5+f6 != "XXXX" and c3+d4+e5+f6 != "OOOO" \
    and d3+e4+f5+g6 != "XXXX" and d3+e4+f5+g6 != "OOOO" \
    and d1+c2+b3+a4 != "XXXX" and d1+c2+b3+a4 != "OOOO" \
    and e1+d2+c3+b4 != "XXXX" and e1+d2+c3+b4 != "OOOO" \
    and f1+e2+d3+c4 != "XXXX" and f1+e2+d3+c4 != "OOOO" \
    and g1+f2+e3+d4 != "XXXX" and g1+f2+e3+d4 != "OOOO" \
    and d2+c3+b4+a5 != "XXXX" and d2+c3+b4+a5 != "OOOO" \
    and e2+d3+c4+b5 != "XXXX" and e2+d3+c4+b5 != "OOOO" \
    and f2+e3+d4+c5 != "XXXX" and f2+e3+d4+c5 != "OOOO" \
    and g2+f3+e4+d5 != "XXXX" and g2+f3+e4+d5 != "OOOO" \
    and d3+c4+b5+a6 != "XXXX" and d3+c4+b5+a6 != "OOOO" \
    and e3+d4+c5+b6 != "XXXX" and e3+d4+c5+b6 != "OOOO" \
    and f3+e4+d5+c6 != "XXXX" and f3+e4+d5+c6 != "OOOO" \
    and g3+f4+e5+d6 != "XXXX" and g3+f4+e5+d6 != "OOOO" \
    or (a1!=" " and a2!=" " and a3!=" " and a4!=" " and a5!=" " and a6!=" " \
    and b1!=" " and b2!=" " and b3!=" " and b4!=" " and b5!=" " and b6!=" " \
    and c1!=" " and c2!=" " and c3!=" " and c4!=" " and c5!=" " and c6!=" " \
    and d1!=" " and d2!=" " and d3!=" " and d4!=" " and d5!=" " and d6!=" " \
    and e1!=" " and e2!=" " and e3!=" " and e4!=" " and e5!=" " and e6!=" " \
    and f1!=" " and f2!=" " and f3!=" " and f4!=" " and f5!=" " and f6!=" " \
    and g1!=" " and g2!=" " and g3!=" " and g4!=" " and g5!=" " and g6!=" "):
        #on vient afficher le puissance 4
        print(f"""
        ____        _                                    __ __
       / __ \__  __(_)_____________ _____  ________     / // /
      / /_/ / / / / / ___/ ___/ __ `/ __ \/ ___/ _ \   / // /_
     / ____/ /_/ / (__  |__  ) /_/ / / / / /__/  __/  /__  __/
    /_/    \__,_/_/____/____/\__,_/_/ /_/\___/\___/     /_/   
                                                            
                        |{a6}|{b6}|{c6}|{d6}|{e6}|{f6}|{g6}|
                         - - - - - - -
                        |{a5}|{b5}|{c5}|{d5}|{e5}|{f5}|{g5}|
                         - - - - - - -
                        |{a4}|{b4}|{c4}|{d4}|{e4}|{f4}|{g4}|
                         - - - - - - -
                        |{a3}|{b3}|{c3}|{d3}|{e3}|{f3}|{g3}|
                         - - - - - - -
                        |{a2}|{b2}|{c2}|{d2}|{e2}|{f2}|{g2}|
                         - - - - - - -
                        |{a1}|{b1}|{c1}|{d1}|{e1}|{f1}|{g1}|
                         ‾ ‾ ‾ ‾ ‾ ‾ ‾
                         a b c d e f g 
        """)
        if t % 2 == False:

            colonne = input("1er joueur met une croix ( X ) en : ")

            # Colonne A
            if colonne == "a" and a1 == " ":
                a1 = "X"
                t = t+1
            elif colonne == "a" and a2 == " ":
                a2 = "X"
                t = t+1
            elif colonne == "a" and a3 == " ":
                a3 = "X"
                t = t+1
            elif colonne == "a" and a4 == " ":
                a4 = "X"
                t = t+1
            elif colonne == "a" and a5 == " ":
                a5 = "X"
                t = t+1
            elif colonne == "a" and a6 == " ":
                a6 = "X"
                t = t+1

            # Colonne B
            elif colonne == "b" and b1 == " ":
                b1 = "X"
                t = t+1
            elif colonne == "b" and b2 == " ":
                b2 = "X"
                t = t+1
            elif colonne == "b" and b3 == " ":
                b3 = "X"
                t = t+1
            elif colonne == "b" and b4 == " ":
                b4 = "X"
                t = t+1
            elif colonne == "b" and b5 == " ":
                b5 = "X"
                t = t+1
            elif colonne == "b" and b6 == " ":
                b6 = "X"
                t = t+1

            # Colonne C
            elif colonne == "c" and c1 == " ":
                c1 = "X"
                t = t+1
            elif colonne == "c" and c2 == " ":
                c2 = "X"
                t = t+1
            elif colonne == "c" and c3 == " ":
                c3 = "X"
                t = t+1
            elif colonne == "c" and c4 == " ":
                c4 = "X"
                t = t+1
            elif colonne == "c" and c5 == " ":
                c5 = "X"
                t = t+1
            elif colonne == "c" and c6 == " ":
                c6 = "X"
                t = t+1

            # Colonne D
            elif colonne == "d" and d1 == " ":
                d1 = "X"
                t = t+1
            elif colonne == "d" and d2 == " ":
                d2 = "X"
                t = t+1
            elif colonne == "d" and d3 == " ":
                d3 = "X"
                t = t+1
            elif colonne == "d" and d4 == " ":
                d4 = "X"
                t = t+1
            elif colonne == "d" and d5 == " ":
                d5 = "X"
                t = t+1
            elif colonne == "d" and d6 == " ":
                d6 = "X"
                t = t+1

            # Colonne E
            elif colonne == "e" and e1 == " ":
                e1 = "X"
                t = t+1
            elif colonne == "e" and e2 == " ":
                e2 = "X"
                t = t+1
            elif colonne == "e" and e3 == " ":
                e3 = "X"
                t = t+1
            elif colonne == "e" and e4 == " ":
                e4 = "X"
                t = t+1
            elif colonne == "e" and e5 == " ":
                e5 = "X"
                t = t+1
            elif colonne == "e" and e6 == " ":
                e6 = "X"
                t = t+1

            # Colonne F
            elif colonne == "f" and f1 == " ":
                f1 = "X"
                t = t+1
            elif colonne == "f" and f2 == " ":
                f2 = "X"
                t = t+1
            elif colonne == "f" and f3 == " ":
                f3 = "X"
                t = t+1
            elif colonne == "f" and f4 == " ":
                f4 = "X"
                t = t+1
            elif colonne == "f" and f5 == " ":
                f5 = "X"
                t = t+1
            elif colonne == "f" and f6 == " ":
                f6 = "X"
                t = t+1

            # Colonne G
            elif colonne == "g" and g1 == " ":
                g1 = "X"
                t = t+1
            elif colonne == "g" and g2 == " ":
                g2 = "X"
                t = t+1
            elif colonne == "g" and g3 == " ":
                g3 = "X"
                t = t+1
            elif colonne == "g" and g4 == " ":
                g4 = "X"
                t = t+1
            elif colonne == "g" and g5 == " ":
                g5 = "X"
                t = t+1
            elif colonne == "g" and g6 == " ":
                g6 = "X"
                t = t+1
            # t = t + 2 pour refaire rejouer la personne
            else:
                t = t + 2
                print("\n1er joueur a jouer dans une colonne pleine, REJOUE !!!!!! ")

        else:
            
            colonne = input("2eme joueur met un rond ( O ) en : ")

            # Colonne A
            if colonne == "a" and a1 == " ":
                a1 = "O"
                t = t+1
            elif colonne == "a" and a2 == " ":
                a2 = "O"
                t = t+1
            elif colonne == "a" and a3 == " ":
                a3 = "O"
                t = t+1
            elif colonne == "a" and a4 == " ":
                a4 = "O"
                t = t+1
            elif colonne == "a" and a5 == " ":
                a5 = "O"
                t = t+1
            elif colonne == "a" and a6 == " ":
                a6 = "O"
                t = t+1

            # Colonne B
            elif colonne == "b" and b1 == " ":
                b1 = "O"
                t = t+1
            elif colonne == "b" and b2 == " ":
                b2 = "O"
                t = t+1
            elif colonne == "b" and b3 == " ":
                b3 = "O"
                t = t+1
            elif colonne == "b" and b4 == " ":
                b4 = "O"
                t = t+1
            elif colonne == "b" and b5 == " ":
                b5 = "O"
                t = t+1
            elif colonne == "b" and b6 == " ":
                b6 = "O"
                t = t+1

            # Colonne C
            elif colonne == "c" and c1 == " ":
                c1 = "O"
                t = t+1
            elif colonne == "c" and c2 == " ":
                c2 = "O"
                t = t+1
            elif colonne == "c" and c3 == " ":
                c3 = "O"
                t = t+1
            elif colonne == "c" and c4 == " ":
                c4 = "O"
                t = t+1
            elif colonne == "c" and c5 == " ":
                c5 = "O"
                t = t+1
            elif colonne == "c" and c6 == " ":
                c6 = "O"
                t = t+1

            # Colonne D
            elif colonne == "d" and d1 == " ":
                d1 = "O"
                t = t+1
            elif colonne == "d" and d2 == " ":
                d2 = "O"
                t = t+1
            elif colonne == "d" and d3 == " ":
                d3 = "O"
                t = t+1
            elif colonne == "d" and d4 == " ":
                d4 = "O"
                t = t+1
            elif colonne == "d" and d5 == " ":
                d5 = "O"
                t = t+1
            elif colonne == "d" and d6 == " ":
                d6 = "O"
                t = t+1

            # Colonne E
            elif colonne == "e" and e1 == " ":
                e1 = "O"
                t = t+1
            elif colonne == "e" and e2 == " ":
                e2 = "O"
                t = t+1
            elif colonne == "e" and e3 == " ":
                e3 = "O"
                t = t+1
            elif colonne == "e" and e4 == " ":
                e4 = "O"
                t = t+1
            elif colonne == "e" and e5 == " ":
                e5 = "O"
                t = t+1
            elif colonne == "e" and e6 == " ":
                e6 = "O"
                t = t+1

            # Colonne F
            elif colonne == "f" and f1 == " ":
                f1 = "O"
                t = t+1
            elif colonne == "f" and f2 == " ":
                f2 = "O"
                t = t+1
            elif colonne == "f" and f3 == " ":
                f3 = "O"
                t = t+1
            elif colonne == "f" and f4 == " ":
                f4 = "O"
                t = t+1
            elif colonne == "f" and f5 == " ":
                f5 = "O"
                t = t+1
            elif colonne == "f" and f6 == " ":
                f6 = "O"
                t = t+1

            # Colonne G
            elif colonne == "g" and g1 == " ":
                g1 = "O"
                t = t+1
            elif colonne == "g" and g2 == " ":
                g2 = "O"
                t = t+1
            elif colonne == "g" and g3 == " ":
                g3 = "O"
                t = t+1
            elif colonne == "g" and g4 == " ":
                g4 = "O"
                t = t+1
            elif colonne == "g" and g5 == " ":
                g5 = "O"
                t = t+1
            elif colonne == "g" and g6 == " ":
                g6 = "O"
                t = t+1
            else:
                t = t + 2
                print("\n2eme joueur a jouer dans une case pleine, REJOUE !!!!!! ")

    # condition si pour choisir le message d'affichage final 
    if a1+b1+c1+d1 != "XXXX" and a1+b1+c1+d1 != "OOOO" \
    and b1+c1+d1+e1 != "XXXX" and b1+c1+d1+e1 != "OOOO" \
    and c1+d1+e1+f1 != "XXXX" and c1+d1+e1+f1 != "OOOO" \
    and d1+e1+f1+g1 != "XXXX" and d1+e1+f1+g1 != "OOOO" \
    and a2+b2+c2+d2 != "XXXX" and a2+b2+c2+d2 != "OOOO" \
    and b2+c2+d2+e2 != "XXXX" and b2+c2+d2+e2 != "OOOO" \
    and c2+d2+e2+f2 != "XXXX" and c2+d2+e2+f2 != "OOOO" \
    and d2+e2+f2+g2 != "XXXX" and d2+e2+f2+g2 != "OOOO" \
    and a3+b3+c3+d3 != "XXXX" and a3+b3+c3+d3 != "OOOO" \
    and b3+c3+d3+e3 != "XXXX" and b3+c3+d3+e3 != "OOOO" \
    and c3+d3+e3+f3 != "XXXX" and c3+d3+e3+f3 != "OOOO" \
    and d3+e3+f3+g3 != "XXXX" and d3+e3+f3+g3 != "OOOO" \
    and a4+b4+c4+d4 != "XXXX" and a4+b4+c4+d4 != "OOOO" \
    and b4+c4+d4+e4 != "XXXX" and b4+c4+d4+e4 != "OOOO" \
    and c4+d4+e4+f4 != "XXXX" and c4+d4+e4+f4 != "OOOO" \
    and d4+e4+f4+g4 != "XXXX" and d4+e4+f4+g4 != "OOOO" \
    and a5+b5+c5+d5 != "XXXX" and a5+b5+c5+d5 != "OOOO" \
    and b5+c5+d5+e5 != "XXXX" and b5+c5+d5+e5 != "OOOO" \
    and c5+d5+e5+f5 != "XXXX" and c5+d5+e5+f5 != "OOOO" \
    and d5+e5+f5+g5 != "XXXX" and d5+e5+f5+g5 != "OOOO" \
    and a6+b6+c6+d6 != "XXXX" and a6+b6+c6+d6 != "OOOO" \
    and b6+c6+d6+e6 != "XXXX" and b6+c6+d6+e6 != "OOOO" \
    and c6+d6+e6+f6 != "XXXX" and c6+d6+e6+f6 != "OOOO" \
    and d6+e6+f6+g6 != "XXXX" and d6+e6+f6+g6 != "OOOO" \
    and a1+a2+a3+a4 != "XXXX" and a1+a2+a3+a4 != "OOOO" \
    and a2+a3+a4+a5 != "XXXX" and a2+a3+a4+a5 != "OOOO" \
    and a3+a4+a5+a6 != "XXXX" and a3+a4+a5+a6 != "OOOO" \
    and b1+b2+b3+b4 != "XXXX" and b1+b2+b3+b4 != "OOOO" \
    and b2+b3+b4+b5 != "XXXX" and b2+b3+b4+b5 != "OOOO" \
    and b3+b4+b5+b6 != "XXXX" and b3+b4+b5+b6 != "OOOO" \
    and c1+c2+c3+c4 != "XXXX" and c1+c2+c3+c4 != "OOOO" \
    and c2+c3+c4+c5 != "XXXX" and c2+c3+c4+c5 != "OOOO" \
    and c3+c4+c5+c6 != "XXXX" and c3+c4+c5+c6 != "OOOO" \
    and d1+d2+d3+d4 != "XXXX" and d1+d2+d3+d4 != "OOOO" \
    and d2+d3+d4+d5 != "XXXX" and d2+d3+d4+d5 != "OOOO" \
    and d3+d4+d5+d6 != "XXXX" and d3+d4+d5+d6 != "OOOO" \
    and e1+e2+e3+e4 != "XXXX" and e1+e2+e3+e4 != "OOOO" \
    and e2+e3+e4+e5 != "XXXX" and e2+e3+e4+e5 != "OOOO" \
    and e3+e4+e5+e6 != "XXXX" and e3+e4+e5+e6 != "OOOO" \
    and f1+f2+f3+f4 != "XXXX" and f1+f2+f3+f4 != "OOOO" \
    and f2+f3+f4+f5 != "XXXX" and f2+f3+f4+f5 != "OOOO" \
    and f3+f4+f5+f6 != "XXXX" and f3+f4+f5+f6 != "OOOO" \
    and g1+g2+g3+g4 != "XXXX" and g1+g2+g3+g4 != "OOOO" \
    and g2+g3+g4+g5 != "XXXX" and g2+g3+g4+g5 != "OOOO" \
    and g3+g4+g5+g6 != "XXXX" and g3+g4+g5+g6 != "OOOO" \
    and a1+b2+c3+d4 != "XXXX" and a1+b2+c3+d4 != "OOOO" \
    and b1+c2+d3+e4 != "XXXX" and b1+c2+d3+e4 != "OOOO" \
    and c1+d2+e3+f4 != "XXXX" and c1+d2+e3+f4 != "OOOO" \
    and d1+e2+f3+g4 != "XXXX" and d1+e2+f3+g4 != "OOOO" \
    and a2+b3+c4+d5 != "XXXX" and a2+b3+c4+d5 != "OOOO" \
    and b2+c3+d4+e5 != "XXXX" and b2+c3+d4+e5 != "OOOO" \
    and c2+d3+e4+f5 != "XXXX" and c2+d3+e4+f5 != "OOOO" \
    and d2+e3+f4+g5 != "XXXX" and d2+e3+f4+g5 != "OOOO" \
    and a3+b4+c5+d6 != "XXXX" and a3+b4+c5+d6 != "OOOO" \
    and b3+c4+d5+e6 != "XXXX" and b3+c4+d5+e6 != "OOOO" \
    and c3+d4+e5+f6 != "XXXX" and c3+d4+e5+f6 != "OOOO" \
    and d3+e4+f5+g6 != "XXXX" and d3+e4+f5+g6 != "OOOO" \
    and d1+c2+b3+a4 != "XXXX" and d1+c2+b3+a4 != "OOOO" \
    and e1+d2+c3+b4 != "XXXX" and e1+d2+c3+b4 != "OOOO" \
    and f1+e2+d3+c4 != "XXXX" and f1+e2+d3+c4 != "OOOO" \
    and g1+f2+e3+d4 != "XXXX" and g1+f2+e3+d4 != "OOOO" \
    and d2+c3+b4+a5 != "XXXX" and d2+c3+b4+a5 != "OOOO" \
    and e2+d3+c4+b5 != "XXXX" and e2+d3+c4+b5 != "OOOO" \
    and f2+e3+d4+c5 != "XXXX" and f2+e3+d4+c5 != "OOOO" \
    and g2+f3+e4+d5 != "XXXX" and g2+f3+e4+d5 != "OOOO" \
    and d3+c4+b5+a6 != "XXXX" and d3+c4+b5+a6 != "OOOO" \
    and e3+d4+c5+b6 != "XXXX" and e3+d4+c5+b6 != "OOOO" \
    and f3+e4+d5+c6 != "XXXX" and f3+e4+d5+c6 != "OOOO" \
    and g3+f4+e5+d6 != "XXXX" and g3+f4+e5+d6 != "OOOO" \
    and (a1!=" " or a2!=" " or a3!=" " or a4!=" " or a5!=" " or a6!=" " \
    or b1!=" " or b2!=" " or b3!=" " or b4!=" " or b5!=" " or b6!=" " \
    or c1!=" " or c2!=" " or c3!=" " or c4!=" " or c5!=" " or c6!=" " \
    or d1!=" " or d2!=" " or d3!=" " or d4!=" " or d5!=" " or d6!=" " \
    or e1!=" " or e2!=" " or e3!=" " or e4!=" " or e5!=" " or e6!=" " \
    or f1!=" " or f2!=" " or f3!=" " or f4!=" " or f5!=" " or f6!=" " \
    or g1!=" " or g2!=" " or g3!=" " or g4!=" " or g5!=" " or g6!=" "):
        print("le jeux est terminer egaliter ")
    elif t % 2 == False:
        print ('''
        

               __                         ___               _     
        ____  / /___ ___  _____  _____   |__ \    _      __(_)___ 
       / __ \/ / __ `/ / / / _ \/ ___/   __/ /   | | /| / / / __ \ 
      / /_/ / / /_/ / /_/ /  __/ /      / __/    | |/ |/ / / / / /
     / .___/_/\__,_/\__, /\___/_/      /____/    |__/|__/_/_/ /_/ 
    /_/            /____/                                         

        
        ''')
    elif t % 2 == True: 
        print('''         
                            
               __                         ___            _         
        ____  / /___ ___  _____  _____   <  /  _      __(_)___ 
       / __ \/ / __ `/ / / / _ \/ ___/   / /  | | /| / / / __ \ 
      / /_/ / / /_/ / /_/ /  __/ /      / /   | |/ |/ / / / / /
     / .___/_/\__,_/\__, /\___/_/      /_/    |__/|__/_/_/ /_/ 
    /_/            /____/                                      


        ''')
    print(f"""

        ____        _                                    __ __
       / __ \__  __(_)_____________ _____  ________     / // /
      / /_/ / / / / / ___/ ___/ __ `/ __ \/ ___/ _ \   / // /_
     / ____/ /_/ / (__  |__  ) /_/ / / / / /__/  __/  /__  __/
    /_/    \__,_/_/____/____/\__,_/_/ /_/\___/\___/     /_/   
                                                            
                        |{a6}|{b6}|{c6}|{d6}|{e6}|{f6}|{g6}|
                         - - - - - - -
                        |{a5}|{b5}|{c5}|{d5}|{e5}|{f5}|{g5}|
                         - - - - - - -
                        |{a4}|{b4}|{c4}|{d4}|{e4}|{f4}|{g4}|
                         - - - - - - -
                        |{a3}|{b3}|{c3}|{d3}|{e3}|{f3}|{g3}|
                         - - - - - - -
                        |{a2}|{b2}|{c2}|{d2}|{e2}|{f2}|{g2}|
                         - - - - - - -
                        |{a1}|{b1}|{c1}|{d1}|{e1}|{f1}|{g1}|
                         ‾ ‾ ‾ ‾ ‾ ‾ ‾
                         a b c d e f g 
        """)