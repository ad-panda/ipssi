nbnotes = int(input("donner nombre de note pour la moyenne : "))
notes = 0 

for i in range(nbnotes):
    notes = float(input("donne moi la note pour faire la moyenne")) + notes

moyenne = (notes) / nbnotes

print(f"la moyenne des notes est de : {moyenne}")