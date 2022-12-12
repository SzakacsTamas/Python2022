import random

#10C
fiuk10C=["Lébár Olivér", "Horváth Hunor", "Szakács Tamás", "Pintér Csongor", "Verbulecz Bence", "Tálas László Martin", "Konyhási Márté", "Keszericze Ákos", "Kiss Gábor", "Holczer Mátyás", "Jankovics Péter", "Jászán Adorján", "Balatincz Martin", "Ivánczi Ferenc", "Haraszti Marcell Leó", "Dobi Levente Domonkos",]
lanyok10C=["Szaszán Vivien Kitti", "Vukk Hanna", "Darus Jázmin Bíborka", "Horváth Andrea","Paizs Patricia","Baranyai Renáta","Török Lilla"]
    

#9H
fiuk9H=["Fasz"]
lanyok9H=["György Lili","Krivarics Hédi Anna","Dergecz Lili"]

#ossz
osszlany=[lanyok9H, lanyok10C]
def egyrandom():
    print()
    szam=(random.randint(0,101))
    kilegyen=str(input("/fiu/ vagy /lany/:"))
    while kilegyen =="fiu":
        fiulegyen=str(input("Ki legyen:"))
        print("A fiú:", fiulegyen,"")
        print("A lány:", random.choice(lanyok9H and lanyok10C))
        print(szam,"%", "illetek össze!")
        kerdes=int(input("Szeretnél még[1=igen, 0=nem]:"))
        if kerdes == 1:
            egyrandom()
        elif kerdes == 0:
            lobby()
    #elif kilegyen == "lany":
    #    lanylegyeb =str(input("Ki legyen:"))
        

egyrandom()


def kuki():
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
        kuki()
        #if ker == 1 :
        #    kuki()
        #elif ker == 0:
        #    lobby()            
            
            
        
        





def kuki2():
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

    kuki2()
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
    if vsztek == 2 :
        kuki()
        print()
    elif vsztek == 1:
        kuki2()
        print()
    


lobby()
