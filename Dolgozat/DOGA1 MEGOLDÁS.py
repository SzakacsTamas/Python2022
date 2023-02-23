def ado(adosav,alapterulet):
    ar=0
    if adosav == "A":
        ar=int(arak[0])*alapterulet
    #print(arak)
    elif adosav == "B":
        ar=int(arak[1])*alapterulet
    else:
        ar=int(arak[2])*alapterulet

    if ar >=10000:
        return ar
    else:
        return  0
        
        

    












f=open("utca.txt")

hazak=[]
for e in f:
    hazak.append(e.replace("\n","").split(" "))

    
    

f.close()

arak=hazak.pop(0)

print("2.feladat A mintában {} telek szerepel".format(len(hazak)))
adoszam=input("3. feladat. Egy tulaj adószáma:")
tulajdonok=[]
for e in hazak:
    if e[0] == adoszam:
        tulajdonok.append(e)

if len(tulajdonok) == 0:
    print("Nem szerepel az adatállományban")
else:
    for e in tulajdonok:
        print("{} utca {}".format(e[1],e[2]))

print(ado("C",120))
hazakA=[e for e in hazak if e[3]== "A"]

hazakB=[]
for e in hazak:
    if e[3] == "B":
        hazakB.append(e)

hazakC=[e for e in hazak if e[3]== "C"]

adoA=[]

for i in range(len(hazakA)):
    hazakA[i].append(ado(hazakA[i][3],hazakA[1][4]))

for i in range(len(hazakA)):
    hazakA[i].append(ado(hazakA[i][3],hazakA[1][4]))



