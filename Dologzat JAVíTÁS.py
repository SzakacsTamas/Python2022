#1 feladat: KÉrj be 10 számot
szamok=[]
#for i in range(10):
#    szamok.append(int(input((str(i+1)) + ". szám: ")))
szamok=[1,2,3,4,5,6,7,8,9,0]
#2
for i in szamok:
    print(str(i), end="")
print()
print("Vége")


#print("".join(szamok))
#3 feladat
for i in range(10):
    print(str(szamok[i])+"\t", end="")
    if i%3==2:
        print()

#4
atlag=sum(szamok)/len(szamok)
print(atlag)

osszeg=0
for i  in szamok:
    osszeg += i
    #osszeg = osszeg + i
atlag=osszeg/len(szamok)
print(atlag)

#5
szoveg="Integer eget pharetra magna. Nulla ex urna, congue ac tincidunt ut, interdum et metus. Phasellus nunc nunc, consectetur eu odio vitae, ullamcorper sagittis nisi. Ut quam tortor, tempus sit amet diam nec, auctor iaculis leo. Donec ut libero velit. Maecenas nisi magna, congue ut tortor quis, maximus maximus arcu. Mauris et commodo nibh. Fusce id est vehicula, consectetur mi et, molestie sapien."
betu="asd"
while betu !="":
    betu=input("Kérek egy betüt: ")
    szoveg=szoveg.replace(betu,betu.upper())

    print(szoveg)

#8
lista=szoveg.split(" ")
lista.reverse()
szoveg2=" ".join(lista)
print(szoveg2)
