import random

#10C
fiuk10C=["Lébár Olivér", "Horváth Hunor", "Szakács Tamás", "Pintér Csongor", "Verbulecz Bence", "Tálas László Martin", "Konyhási Márté", "Keszericze Ákos", "Kiss Gábor", "Holczer Mátyás", "Jankovics Péter", "Jászán Adorján", "Balatincz Martin", "Ivánczi Ferenc", "Haraszti Marcell Leó", "Dobi Levente Domonkos",]
lanyok10C=["Szeszán Vivien Kitti", "Vukk Hanna", "Darus Jázmin Bíborka", "Horváth Andrea","Paizs Patricia","Baranyai Renáta","Török Lilla"]
    

#9H
fiuk9H=["Fasz"]
lanyok9H=["György Lili","Krivarics Hédi Anna","Dergecz Lili"]

#ossz
osszlany=[lanyok9H, lanyok10C]


def kmk():
    vsz=int(input("Hogyan szeretnél[csak fiúk=1, csak lányok=2, teljesen random=3]:"))
    if vsz == 1 :
        print("1=kiss/2=marry/3=kill")
        for i in range(3):
            print(random.choice(fiuk10C + fiuk9H))
        print(i+1)
        input("")

kmk()





#CSAK EGY EMBER RANODM LEHET FIU/LANY
def egyrandom():
    print()
    szam=(random.randint(0,101))
    kilegyen=str(input("/fiu/ vagy /lany/:"))
    if kilegyen == "fiu":
        fiulegyen=str(input("A fiú:"))
        print("A lány:", random.choice(lanyok9H + lanyok10C))
        print(szam,"%", "illetek össze!")
        kerdes=int(input("Szeretnél még[1=igen, 0=nem]:"))
        print()
        if kerdes == 0:
                lobby()
        while kerdes == 1:
            szam=(random.randint(0,101))
            print("A fiú:", fiulegyen)
            print("A lány:", random.choice(lanyok9H + lanyok10C))
            print(szam,"%", "illetek össze!")
            kerdes=int(input("Szeretnél még[1=igen, 0=nem]:"))
            print()
            if kerdes == 0:
                lobby()
    elif kilegyen == "lany":
        lanylegyen=str(input("A lány neve:"))
        print("A fiú:", random.choice(fiuk9H + fiuk10C))
        print(szam,"%", "illetek össze!")
        kerdes=int(input("Szeretnél még[1=igen, 0=nem]:"))
        print()
        while kerdes == 1:
            szam=(random.randint(0,101))
            print("A lány:", lanylegyen)
            print("A fiú:", random.choice(fiuk9H + fiuk10C))
            print(szam,"%", "illetek össze!")
            kerdes=int(input("Szeretnél még[1=igen, 0=nem]:"))
            print()
            if kerdes == 0:
                lobby()
        
    #elif kilegyen == "lany":
    #    lanylegyeb =str(input("Ki legyen:"))
        
#def csakfiu():
#    szam=(random.randint(0,101))
#    print("A fiú:", "asd","")
 #   print("A lány:", random.choice(lanyok9H and lanyok10C))
 #   print(szam,"%", "illetek össze!")
#    kerdes=int(input("Szeretnél még[1=igen, 0=nem]:"))
 #   if kerdes == 1:
#        csakfiu()
  #  elif kerdes == 0:
 #       lobby()



#NÉVMEGADÁS
def nevmeg():
        print()
        print("[Kilépés, két érték=0]")
        kivagy=input("Ki vagy te:")
        ki=input("Ki legyen a párod:")
        szam=(random.randint(0,101))
        szazalek=100
        #if kivagy=="Tomi" and ki=="Hédi":
        #    print(szazalek, "%", "Illetek Össze!")
        #elif kivagy =="Hédi" and ki=="Tomi":
        #    print(szazalek, "%", "Illetek Össze!")
        #else:
        #if kivagy and ki == str:
        #   print(szam, "%", "Illetek össze!")
        #if kivagy and ki != str:
        #if kivagy and ki != str:
            
        #        print("Ezek nem emberek! Írj be rendes neveket!")
        #        print()
        #        kuki()
        ##        
        
        if kivagy and ki != "0":
            
            print(szam, "%", "Illetek össze!")
        #ker=int(input("Akarsz még játszani? (igen=1, nem=0):"))
        print()
        
        if kivagy and ki == "0":
            lobby()
        nevmeg()  
#MINDENRANDOM
def mindenran():
    print()

    
    szam=(random.randint(0,101))
    print("A fiú:", random.choice(fiuk10C + fiuk9H))
    print("A lány:", random.choice(lanyok10C + lanyok9H))
    print(szam, "%", "Illetek össze")
    vsz=int(input("Akarsz még(igen=1, Nem=0):"))
    if vsz == 1:
        mindenran()
    elif vsz ==0:
        
    
        lobby()
        print()


            
        
        




#OSZTALYMEGADÁS
def osztmeg():
    print()
    print("[Kilépés, két érték=0]")

    
    szam=(random.randint(0,101))
    kerfiu=str(input("Hova jár a fiú?:"))
    kerlany=str(input("Hova jár a lány?:"))
    c10="10c" or "10C"
    h9="9h" or "9H"
    if kerfiu == c10:
        print("A", kerfiu, "-s", "Fiú:", random.choice(fiuk10C))
    elif kerfiu == h9:
        print("A", kerfiu, "-s", "Fiú:", random.choice(fiuk9H))

    if kerlany == h9:
        print("A", kerlany, "-s", "Lány:", random.choice(lanyok9H))
    elif kerlany == c10:
        print("A", kerlany, "-s", "Lány:", random.choice(lanyok10C))

    if kerlany and kerfiu != "0":
        print(szam, "%", "Illetek össze")
    print()
    if kerlany and kerfiu == "0":
        lobby()

    osztmeg()
    #asd=int(input("Akarsz még egyet?(igen=1, nem=0):", ))
    #print()
    #if asd == 1:
    #    kuki2()
    #elif asd == 0:
    #    lobby()

        

def lobby():
    eloszt=int(input("Milyen Játékot szeretnél játszani?[1.Szerelem Gép]:"))
    if eloszt == 1:
        vsztek=int(input("És hogyan szeretnél (1. Random emberek, 2. Névmegadás)"))
    if vsztek == 1 :
        vsztek2=int(input("Csak az egyik név random[1], Minden Random[2], osztálymegadás[3], csak fiúk[4]:"))
        if vsztek2 == 1:
            egyrandom()
            print()
        elif vsztek2 == 2:
            mindenran()
            print()
        elif vsztek2 == 3:
            osztmeg()
            print()
        #elif vsztek2 == 4:

            
    elif vsztek == 2:
        nevmeg()
        print()
    


lobby()
