import rock_paper_scissors
import random

#2022/03/02
#Csapat tagok: Darusi Jázmin Bíborka, Jászán Adojrán, Szakács Tamás


iskola=["Iskola","szivacs","kréta","tanár","diák","tábla","tanterem","tornaterem","büfé","tanulás","tananyag"]
emlos_allatok=["Emlős Állatok","medve","zsiráf","egér","mókus","szarvasmarha","oroszlán","panda","farkas","szurikáta","tehén"]
hullok_allatok=["Hüllők","gyík","kameleon","varánusz","kígyó","gekko","krokodil","teknős","agáma","dinoszaurusz","sikló",]
vizi_allatok=["Vizi Állatok","cápa","rák","tonhal","keszeg","ponty","gömbhal","kagyló","tintahal","angolna","homár","plankton","tengeri csillag"]
zoldseg=["Zöldségek","répa","burgonya","cékla","saláta","uborka","padlizsán","retek","paprika","paradicsom","borsó","bab","hagyma"]
gyumolcs=["Gyümölcsök","nektarin","málna","dinnye","kiwi","citrom","mangó","eper","narancs","ananász","alma"]
targyak=["Iskolai Tárgyak","toll","ceruza","papír","ragasztó","olló","radír","hibajavító","szöveg kiemelő","matrica","hegyző"]
erzesek=["Érzések","harag","irigység","szerelem","magány","öröm","bizalom","szomorúság","undor","rettegés","félelem"]

temak=iskola,emlos_allatok,hullok_allatok,vizi_allatok,zoldseg,gyumolcs,targyak,erzesek

betuk=["a", "á", "b", "c", "d", "e","é", "f", "g", "h", "i", "í", "j", "k", "l", "m", "n", "o", "ó", "ö", "ő", "p", "q", "r", "s", "t", "u", "ú", "ü", "ű", "v", "w", "x", "y", "z"]



def jatek():
    
    random_tema=random.choice(temak)
    random_szo=random.choice(random_tema[1:])
    rossz_tipp=0
    lista_neve = random_tema
    
    kerdes=""
    #print(random_szo)
    hasznalt_betu=[]
    if len(random_szo) > 9:
        tippek= random_szo[:3] + "-" * (len(random_szo) - 3)
    elif len(random_szo) > 7:
        tippek= random_szo[:2] + "-" * (len(random_szo) - 2)
    elif len(random_szo) > 4:
        tippek= random_szo[0] + "-" * (len(random_szo)-1)

    
    else:
        tippek= "-" * len(random_szo)
    
    
    print("Kezdődjön a köröd!")
    
    print("A Témád |" + random_tema[0] +"|")
    print("A szavad |" + str(len(random_szo)) +"| karakter hosszú.")
      
    #print(random_szo)
    
        
    
    bekert_betu=""
    #if bekert_betu.isalpha():
    while rossz_tipp < 10 and "-" in tippek and random_szo != bekert_betu:
        #print("-"*40)
        print("*"*len(random_szo))    
        #if len(random_szo) > 5:
        #    tippek=random_szo[0] + "-" * (len(random_szo) - 1)
        #    tippek=str(tippek)
        print(tippek)
            
        #else:
        #    print(tippek)
        print("*"*len(random_szo))
        print("-"*40)
        bekert_betu=input("Kérj be egy betűt & írd be a szót: ")
        if bekert_betu.isalpha():
            bekert_betu=str(bekert_betu)
            if bekert_betu in random_szo:
                
                for i in range(len(random_szo)):
                    if random_szo[i] == bekert_betu:
                        print("_"*40)
                        print("Ezeket használtad fel: |" + ",".join(hasznalt_betu) + "|")
                        print("Van benne!")
                        tippek = tippek[:i] + bekert_betu + tippek[i+1:]
                    elif random_szo == bekert_betu:
                        print("Kitaláltad!")
                        break
                    
                
            else:
                if bekert_betu not in hasznalt_betu :
                        hasznalt_betu.append(bekert_betu)
                        print("_"*40)
                        print("|" + str(9-rossz_tipp) +"| próbálkozásod maradt. "+ "|" + random_tema[0]+"|")
                        print("Ezeket használtad fel: |" + ",".join(hasznalt_betu) + "|")
                        print("Nincs Benne!")
                        rossz_tipp +=1
                        
                else:
                    print("_"*40)
                    print("Már használtad ezt a betüt")
                    print("Ezeket használtad fel: |" + ",".join(hasznalt_betu) + "|")
                
                    
              
        else:
            print("Ez nem egy betű, újra!")
            
    if "-" not in tippek:
        print("Nyertél!")
        print("*"*len(random_szo))    
        print(random_szo)
        print("*"*len(random_szo))
    elif random_szo == bekert_betu:
        print("*"*len(random_szo))    
        print(random_szo)
        print("*"*len(random_szo))
    else:
        print("Vesztettél!")
        print("*"*len(random_szo))    
        print(random_szo)
        print("*"*len(random_szo))
    print("-"*40)
    while True:
        kerdes = input("Szeretnél még játszani? [igen,nem]: ")
        if kerdes.isalpha():
            kerdes=str(kerdes)
            if kerdes== "igen":
                
                print()
                jatek()
            
            elif kerdes== "nem":
                print("_"*40)
                fomenu()
    
            else:
                print("Csak mond hogy |igen| vagy |nem|.")
                print("-"*30)
        else:
            print("Csak szöveget írhatsz be!, újra")
            print()
    

def fomenu():
    while True:
    

        kerdes = input("Milyen játékot szeretnél játszani? [akasztófa | dzsanken(Kő,Papír,Olló)]: ")
        if kerdes.isalpha():
            kerdes=str(kerdes)
            if kerdes== "akasztófa":
                print()
                menu1()
                break
            elif kerdes== "dzsanken":
                print()
                rock_paper_scissors()
                break

            else:
                print("A felsorolt lehetőségek közül válassz |akasztófa| vagy |kő papír olló|.")
                print("_"*70)
        else:
            print("Csak szöveget fogadok el, újra!")
            print("-"*30)
    
#Akasztófa menüje    
def menu1():
    print("*"*11)
    print(" AKASZTÓFA")
    print("*"*11)
    print()
    lehetoseg=0
    while True:
    
        #try:
        kezdes = input("Kezdhetjük a játékot? [igen,nem]: ")
        if kezdes.isalpha():
            kezdes=str(kezdes)
            if kezdes== "igen":
                print()
                jatek()
                break
            elif kezdes== "nem":
                if lehetoseg < 1:
                    
                    print("Na akkor megkérdezem mégegyszer...")
                print("-"*35)
                lehetoseg+= 1
                if lehetoseg == 2:
                    
                    
                    print()
                    fomenu()
                    break
                    
            else:
                print("Csak mond hogy |igen| vagy |nem|.")
                print("-"*30)
        else:
            print("Csak szöveget fogadok el, újra!")
            print("-"*30)
                #except:
            #print("hiba")


#jatek()



fomenu()


#for i in range(20):




    #print(random_szo)



#végigfut a szón
#for e in random_szo:
#    print(e)

#Eltünteti a space-t, de a szövegben nem hagy üresen egy alsó vonást, csak kihagyja és megy tovább(Az egész egybe lesz)
#random_szo="egy egy"
#print(random_szo)
#print(len(random_szo))
#random_szo=random_szo.replace(" ","")
#print(len(random_szo))
#tippek="_ "*len(random_szo)
#print(tippek)
