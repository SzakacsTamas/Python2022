from feladatmodul import teglalap

keruletek=[]
teruletek=[]
for i in range(5):
    szel=int(input("Kérem a téglalap szélességét: "))
    hossz=int(input("Kérem a téglalap hosszúságát: "))

    tegla1=teglalap(szel,hossz)
    tegla1.kerulet()
    keruletek.append(tegla1.kerulet)
    tegla1.terulet()
    teruletek.append(tegla1.terulet)

print(keruletek)
print(teruletek)
