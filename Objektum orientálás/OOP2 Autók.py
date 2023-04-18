#legyen tulajdonsága: pl Szín
#ajtók száma
#Márka jelzés és típus jelzés
#Tudjon indulni, induláskor mondja azt hogy "brrr"
#legyen rajta duda "TüTü"
#Irányjelző ami azt mondja "KatKatKat"
#Leszármazott ami BMW induljon úgy hogy "Brumm",irányjelző legyen Néma
#Másik leszármazott Mercedes néven, a duda legyen valami MÁS
#3. Autó, legyen Audi, check engine legyen hamis, NINCS BEKAPCSOLVA, de ha megnyomják a dudát, elromlik a motor
class auto:
    márka,szín,ajtók_száma,típus=["","",0,""]
    def __init__(self,márka,szín,ajtók_száma,típus):
        self.márka=márka
        self.szín=szín
        self.ajtók_száma=ajtók_száma
        self.típus=típus
    def duda(self):
        print("TüTü")

    def indul(self):
        print("BRRrrrr")
    def iranyjelzo(self):
        print("KatKatKat")
        

k1=auto("Toyota","Piros",5,"Kuki")

k1.duda()
