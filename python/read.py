file = str
nom = str(input("donne le nom du fichier a lire : "))

with open(nom , "r") as file:
    print(file.readline())

print(f"le fichier {nom} est afficher")

