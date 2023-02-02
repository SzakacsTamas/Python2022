import random
f=open("felszam.txt","r")


kerdesek=[]
for sor in f:
    josor=sor.replace("\n","")
    josor2=f.readline().replace("\n","")
    temp=josor2.split(" ")
    kerdesek.append([josor,int(temp[0]),int(temp[1]),temp[2]])
    
  

f.close()
print("2. feladat")
print("Az adatfile-ban " + str(len(kerdesek)) + " kérdés van.")

matek=[]
for e in kerdesek:
    if e[3] == "matematika":
        matek.append(e[2])


print("Az adatfajlban " + str(len(matek)) +
      " matematika feladat van, 1 pontot er " + str(matek.count(1)) + " feladat, 2 pontot er " + str(matek.count(2)) +
      " feladat, 3 pontot er " + str(matek.count(3)) + " feladat.")


valaszok=[]
for e in kerdesek:
    valaszok.append(e[1])

valaszok=[e[1] for e in kerdesek]
print("A válaszok szám értéke {}-től {}-ig tart.".format(min(valaszok),max(valaszok)))

temakorok=[]
for e in kerdesek:
    if e[3] not in temakorok:
        temakorok.append(e[3])

print()
print("5.Feladat")  #    I  
#                        V   EZZEL A STRING-el FŰZD ÖSSZE A LISTA ELEMEIT
print("A témakörök: " + ", ".join(temakorok))
    
print("6. Feladat")


beker=input("Milyen Témakörből szeretne kérdést kapni? ")
ujLista=[e for e in kerdesek if e[3]== beker]
print(ujLista)

sorsolt=random.choice(ujLista)
valasz=input(sorsolt[0])
if int(valasz)== sorsolt[1]:
    print(str(sorsolt[2]) + " pont")
else:
    print("0 pont"  + str(sorsolt[1]) + "pont")







