#loop=int(input("Hányszor akarsz loop-olni?: "))
#Min=int(input("Mennyi legyen a min?: "))
#Max=int(input("Mennyi legyen a max?: "))
#for i in range(loop):
import random

#    print(random.randint(Min, Max))


def kuki():
    for i in range(100):
        kivagy=str(input("Ki vagy te?: "))
        ki=str(input("Ki legyen a Párod?: "))
        szam=(random.randint(0,101))
        szazalek=100
        if kivagy=="Tomi" and ki=="Hédi":
            print(szazalek, "%", "Illetek Össze!")
        elif kivagy =="Hédi" and ki=="Tomi":
            print(szazalek, "%", "Illetek Össze!")
        else:
            print(szam, "%", "Illetek össze !:D")
        

kuki()

