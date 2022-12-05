#loop=int(input("Hányszor akarsz loop-olni?: "))
#Min=int(input("Mennyi legyen a min?: "))
#Max=int(input("Mennyi legyen a max?: "))
#for i in range(loop):
import random
szam=(random.randint(0,101))
fiuk=["Olcsi", "Huni", "Tomi", "Csocsi", "Bence", "LaciMaci", "Konyhi", "Magas", "BMW", "Vak", "Petyko", "Ady", "Martinez(Budos)", "Ferko", "Marci", "Levike"]
Lányok=["Vivike", "Hanna(Nagy)", "Hanna(ViviWhite)", "Jázmin", "Andi", "Hédi","J1","J2"]
#print(random.randrange(3, 9))
#    print(random.randint(Min, Max))
def kuki2():
    for i in range(100):
        boys=(random.choice(fiuk))
        girls=(random.choice(Lányok))
    print("A fiú:", boys)
    print("A Lány:", girls)
    print(szam, "%", "Illetek össze")
    asd=int(input("Akarsz még egyet?(igen=0):" ))
    if asd == 0:
        kuki2()
kuki2()
        

def kuki():
    for i in range(100):
        kivagy=str(input("Ki vagy te?: "))
        ki=str(input("Ki legyen a Párod?: "))
        
        szazalek=100
        if kivagy=="Tomi" and ki=="Hédi":
            print(szazalek, "%", "Illetek Össze!")
        elif kivagy =="Hédi" and ki=="Tomi":
            print(szazalek, "%", "Illetek Össze!")
        else:
            print(szam, "%", "Illetek össze !:D")
        

#kuki()

