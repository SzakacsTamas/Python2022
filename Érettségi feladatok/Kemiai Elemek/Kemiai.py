f=open("felfedezesek.csv")
elemek=[]

for e in f:
    elemek.append(e.replace("\n","").split(";"))
    



f.close()
elemek.pop(0)



print("3. feladat: Elemek száma : {}".format(len(elemek)))


okor=[e for e in elemek if e[0]=="Ókor"]




print("4. feladat: Felfedezések száma az ókorban : {}".format(len(okor)))

print("5 Feladat")
while True:
    vegyjel=input("Kérek egy vegyjelet: ".lower())
    if len(vegyjel)<3 and len(vegyjel) >0:
        jo=True
        for i in range(len(vegyjel)):
            if not (vegyjel[i] >= "a" and vegyjel[i] <="z"):
                jó=False
        if jo:
            break

#print(vegyjel)


print("6. Feladat")
keresett=[e for e in elemek if e[2].lower()==vegyjel]
if keresett ==[]:
    print("Nincs ilyen elem")
else:
    print(keresett)

