import os
import sys
import random

def fct_justeprix():

    a = int(input("donner le chiffre le plus bas : "))
    b = int(input("donner le chiffre le plus haut : "))

    secret = random.randrange(a, b, 1)
    i = int
    tab = 0

    os.system('cls||clear')

    while i != str(secret) and i != 'a':

        i = (input("essaye de trouver le Juste prix : "))
        tab = tab + 1

        if i == "a": 
            print("vous avez abandonner ")
        elif i == str(secret):print(f"tu as trouver au bout de {tab} fois !!! trop fort !!!")
        else: print("reessaye encore une fois ou marque a pour abandonner ")
