
#calcul de la somme de 2 carres 

def somme_des_carres(x,y):
    '''retourne la somme de x au carre et y a carre'''
    return x*x + y*y 


#programme principal

nombre1 = int(input("donne le premier chiffre de la somme des carre : "))
nombre2 = int(input("donne le deuxieme chiffre de la somme des carre : "))
somme_des_carres(nombre1,nombre2)