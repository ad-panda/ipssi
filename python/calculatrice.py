


def fct_calculatrice():

    a = float(input("donner le premier nombre :"))
    b = float(input("donner le second nombre :"))

    operateur = str(input("donner l'oepration a faire :"))

    if      operateur == "+":
            c = a + b
            print(f"la somme est egale a : {c}")

    elif    operateur == "-":
            c = a - b
            print(f"la soustraction est egale a : {c}")

    elif    operateur == "%":
            c = a % b
            print(f"le modulo est egale a : {c}")

    elif    operateur == "/":
            c = a / b
            print(f"la division est egale a : {c}")

    elif    operateur == "*":
            c = a * b
            print(f"la multiplication est egale a : {c}")
