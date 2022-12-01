def oszlopba(munkalista, db):
    for i in range(len(munkalista)):
        print(munkalista[i], "", end="")
        if i%db == db-1:
            print()
    print()

    
lista=[]

for i in range(0):
    
    lista.append(int(input("Kérj be egy szamot: ")))
lista=[1,2,3,4,5,6,7,8,9,10]
print(lista)


for i in range(len(lista)):
    print(lista[i], "", end="")
    if i%3 == 2:
        print()
print()


szambe=int(input("Kerek egy intet: "))
if szambe in lista:
    print("Van benne!")
else:
    
    print("Nincs Benne!")


oszlopba(lista, 5)
