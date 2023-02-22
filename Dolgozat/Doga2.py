f=open("tancrend.txt","r")

#print(f.read())
print("2. Feladat")
 
tancok=[]
for i in f:
    #tancok.append(i)
    a=i.replace("\n","").split(";")
    tancok.append(a)
print(tancok[0])
print(tancok[-3])
#print(tancok)



print("3. Feladat")
#for e in tancok:
i=tancok[::3]
#print(i)
a=i.count(['samba'])
print(str(a)+ " Pár táncolt szambát")


#for e in tancok(3):
#   print(e)
    

#print(tancok)
#sambaSzam=tancok.count("cha-cha")
#print(sambaSzam)
#for e in tancok:
#    e.count

f.close()
#temp=egySor.replace("\n","").split(";")

