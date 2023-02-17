import Feladat2

def ujabb(darab=3):
    haromszogek=[]
    for i in range(darab):
        haromszogek.append(Feladat2.haromszog())

    for e in haromszogek:
        print("\ta={}, b={}, c={}".format(e[0],e[1],e[2]))
    return haromszogek

def haromszogE(haromszogek):
    for e in haromszogek:
        if sum(e)-max(e) > max(e):
            print("Lehet Háromszög!")

        else:
            print("Nem lehet Háromszög!")

h=ujabb(3)
haromszogE(h)
#lista=Feladat2.haromszog()
#print(lista)
