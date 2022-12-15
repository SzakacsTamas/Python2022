import random
import math

minimumErtek=int(input("Add meg, hogy hol kezdődjön: "))
maximumErtek=int(input("Add meg, hogy hol legyen vége: "))
darab=int(input("Mennyi darab kell: "))

lista=[]

for i in range(darab):
    lista.append(random.randint(minimumErtek, maximumErtek))
    


print(lista)

legnagyobb=max(lista)
egyseg=80//legnagyobb

for e in lista:
    #print(e,end=""+"\t")
    print("*"* (e * egyseg))
