



def fct_morpion():

    a = " "
    b = " "
    c = " "
    d = " "
    e = " "
    f = " "
    g = " "
    h = " "
    i = " "
    t = 0
    pos2 = str

    while a + b + c != "XXX" and a + b + c != "OOO" and d + e + f != "XXX" and d + e + f != "OOO" and g + h + i != "XXX" and g + h + i != "OOO" and a + d + g != "XXX" and a + d + g != "OOO" and b + e + h != "XXX" and b + e + h != "OOO" and c + f + i != "XXX" and c + f + i != "OOO" and a + e + i != "XXX" and a + e + i != "OOO" and g + e + c != "XXX" and g + e + c != "OOO" or ((a or b or c or d or e or f or g or h or i ) == " "):
        print(f'''
    {a} | {b} | {c}
    --|---|--
    {d} | {e} | {f}
    --|---|--
    {g} | {h} | {i} ''')
        if t % 2 == False:

            pos2 = input("1er joueur met une croix ( X ) en : ")

            if  pos2 == "a" and a == " ":
                a = "X"
                t = t+1
            elif    pos2 == "b" and b == " ":
                b = "X"
                t = t+1
            elif    pos2 == "c" and c == " ":
                c = "X"
                t = t+1
            elif    pos2 == "d" and d == " ":
                d = "X"
                t = t+1
            elif    pos2 == "e" and e == " ":
                e = "X"
                t = t+1
            elif    pos2 == "f" and f == " ":
                f = "X"
                t = t+1
            elif    pos2 == "g" and g == " ":
                g = "X"
                t = t+1
            elif    pos2 == "h" and h == " ":
                h = "X"
                t = t+1
            elif    pos2 == "i" and i == " ":
                i = "X"
                t = t+1
            else:
                t = t + 2
                print("\n1er joueur a jouer dans une case pleine, REJOUE !!!!!! ")

        else:
            
            pos2 = input("2eme joueur met un rond ( O ) en : ")

            if  pos2 == "a" and a == " ":
                a = "O"
                t = t+1
            elif    pos2 == "b" and b == " ":
                b = "O"
                t = t+1
            elif    pos2 == "c" and c == " ":
                c = "O"
                t = t+1
            elif    pos2 == "d" and d == " ":
                d = "O"
                t = t+1
            elif    pos2 == "e" and e == " ":
                e = "O"
                t = t+1
            elif    pos2 == "f" and f == " ":
                f = "O"
                t = t+1
            elif    pos2 == "g" and g == " ":
                g = "O"
                t = t+1
            elif    pos2 == "h" and h == " ":
                h = "O"
                t = t+1
            elif    pos2 == "i" and i == " ":
                i = "O"
                t = t+1
            else:
                t = t + 2
                print("\n2eme joueur a jouer dans une case pleine, REJOUE !!!!!! ")

    if a + b + c != "XXX" and a + b + c != "OOO" and d + e + f != "XXX" and d + e + f != "OOO" and g + h + i != "XXX" and g + h + i != "OOO" and a + d + g != "XXX" and a + d + g != "OOO" and b + e + h != "XXX" and b + e + h != "OOO" and c + f + i != "XXX" and c + f + i != "OOO" and a + e + i != "XXX" and a + e + i != "OOO" and g + e + c != "XXX" and g + e + c != "OOO" and ((a or b or c or d or e or f or g or h or i ) != " "):
        print("le jeux est terminer egaliter ")
    elif t % 2 == False:
        print("Le 1er joueur a gagner !!!!")
    elif t % 2 == True: 
        print ("le deuxieme joueur a gagner")
    print(f'''
    {a} | {b} | {c}
    --|---|--
    {d} | {e} | {f}
    --|---|--
    {g} | {h} | {i} ''')