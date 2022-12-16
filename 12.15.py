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
    print("*"*math.floor(e * egyseg))


#jegyű szám bekeres
szam="1"
while len(szam) != 3:
    
    
    

    szam=input("Kérj be egy 3 jegyű szzámot:")
#print(type(szam))
szam=int(szam)
#print(type(szam))
if szam % 12 == 0:
    print("osztható")
print(szam)


szoveg="ontrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.1orum et Malorums book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32."
print(len(szoveg.split(" ")))
betu=str(input("KÉrj be egy betut:"))
szoveg2=szoveg.replace(betu, betu.upper())
print(szoveg2)

