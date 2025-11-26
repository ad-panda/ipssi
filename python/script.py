import sys
import os
import random
import calculatrice
import puissance4
import justeprix

def ajouter_note():
    note = input("entrez une nouvelle note : ")
    with open("note.txt", "a") as f:
        f.write(note + "\n")

def lire_notes():
    with open("note.txt", "r") as f:
        print(f.read())

choix = str

while choix != "q":

    choix = str(input('''
      Menu :

      n - Entrer une nouvelle note
      l - lire une note
      c - calculatrice
      p - puissance4
      j - juste prix
      q - quitter

        Votre choix : '''))

    print(f"vous avez choisi : {choix}")

    if choix == "n": ajouter_note()

    elif choix == "l": lire_notes()

    elif choix == "c": calculatrice.fct_calculatrice()

    elif choix == "p": puissance4.fct_puissance4()

    elif choix == "j": justeprix.fct_justeprix()




