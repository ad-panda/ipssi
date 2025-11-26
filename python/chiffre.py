a = int(input("donner un chiffre : "))
b = int(input("donner un seconde chiffre : "))
c = int(input("donner un troisieme chiffre : "))

if a >= b and a >= c:
    print('LE MAX EST : ', a)

elif b >= a and b >= c:
    print("le max est : ", b)
    
else: print("le max est : ", c)