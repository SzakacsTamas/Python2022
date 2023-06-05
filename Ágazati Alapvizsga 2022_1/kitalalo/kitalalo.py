import modul
import random
lista=[]
f=open("szavak.txt")

for e in f:
    lista.append(e.replace('"',"").strip())

f.close()

sorok=lista[0].split(", ")

#print(sorok)


szavak=[]
for a in sorok:
    szavak.append(modul.szo(a))


#print(szavak)

rejtett=random.choice(szavak)
print(rejtett.szo)

tippek=[]
while True:
    be=input("Kérek egy szót(6.betűs): ")
    tippek.append(be)
    if be=="stop":
        break

    vissza=rejtett.minta(be)
    print("Az eredmény: {}".format(vissza))
    if vissza ==be:
        break
    
if tippek[-1]=="stop":
    pass
else:
    print("{} tipeléssel sikerlüt kitaléáál".format(len(tippek)))

