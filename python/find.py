import os

a = int(input("donne moi le chiffre a trouver"))
i = int

os.system('cls||clear')

while i != a:
    i = int(input("essaye de trouver le chiffre : "))
    if i == a:
        print("tu as trouver !!! trop fort !!!")
    else: print("reessaye encore une fois ")
