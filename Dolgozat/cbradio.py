szovegesAdatok=[]
f=open("cb.txt")

for sor in f:
    szovegesAdatok.append(sor.strip().split(";"))
szovegesAdatok.pop(0)
print(szovegesAdatok)
f.close()

class adatok:
    def __init__(self,sor):
        vag=sor.strip().split(";")
        self.ora=vag[0]
        self.perc=vag[1]
        self.adasdb=vag[2]
        self.nev=vag[3]
        
    def kiirat(self):
        print(vag)

    #def beolvas(self):

    





print("3. feladat: Bejegyzések száma {} db".format(len(szovegesAdatok)))



for i in szovegesAdatok:
            #print(i[2])
             
    if i[2]=="4":
        print("4. feladat: Volt négy adást indító sofőr.")
        break
else:
    print("4. feladat: Nem volt négy adást indító sofőr")

nevek=[]
for e in szovegesAdatok:
    nevek.append(e[3])
#print(nevek)
beker=input("5. feladat: Kérek egy nevet: ")
if beker in nevek:
    print("Benne van")
    print(beker,0 , "használta a CB-rádiót")
else:
    print("Nem")


#for e in szovegesAdatok:
#    print(e.split(";"))
    #print(e[0])
    #print(e)
    

#("6. feladat")

#def AtszamolPercre():
    
  
#    print(szovegesAdatok)

#AtszamolPercre()


print("8. feladat: sofőrök száma: ")
print("9. feladat: Legtöbb adást indító sofőr")
