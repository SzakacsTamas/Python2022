f=open("utca.txt","r")

#print(f.read())
szoveg=[]
for i in f:
    szoveg.append(i)
szoveg.pop(0)
print(szoveg)


    #tordelt= str(i.split(" ",""))


    
print("2. feladat. A mintában " + str(len(szoveg)) + " telek szerepel")

#("3. feladat. Egy tulajdonos adószáma: ")

for i in szoveg:
    for list in i.split(" "):
    
tulaj=input("Egy tulajdonos adószáma:")
if tulaj in tor:
    print("Benne van")
else:
    print("Nincs benne")

f.close()

