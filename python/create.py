
annotation = str(input("ecris ce que tu veux mettre dans le fichier note.txt : "))
nom = str(input("taper le nom du fichier et extension(.txt,.py etc...)"))

with open(nom , "w") as file:
    file.write(annotation)

print(f"le fichier {nom} est creer")

