import random
import math

szavak=["alma","körte","barack","banón","dinnye","szőlő"]

#random.seed(1)
print( szavak[random.randint(0,len(szavak)-1)])

print(random.choice(szavak))

#[["alma",14], ["körte", 18], []...]

nagyLista=[]
for e in szavak:
    print("-"*20)
    kisLista=[]
    kisLista.append(e)
    kisLista.append(random.randint(12,312))
    print(kisLista)
    nagyLista.append(kisLista)

print(nagyLista)



for e in nagyLista:
    print(e[0].ljust(10),str(e[1]).rjust(4),"kg")
