#Modul készítés, a modul tartalmazzon egy osztályt teglalap néven,2 adat, hosszúság, szélesség
#két fuggvény, terulet,kerulet számítás
#Kérjünk be 5 téglalapo adatát egy másik fájlba
#irjuk ki amelyik a legnagyobb területű ás kerületű
class teglalap():
    def __init__(self,szelesseg,hosszusag):
        self.szelesseg=szelesseg
        self.hosszusag=hosszusag

    def terulet(self):
        print("A téglalap kerülete: ",self.szelesseg*self.hosszusag,"cm²")
    def kerulet(self):
        print("A téglalap területe: ", 2*(self.szelesseg+self.hosszusag),"cm")
    def adatok(self):
        print("A tégla széle és hossza: ", self.szelesseg, self.hosszusag)

#tegla1=teglalap(15,40)

#tegla1.terulet()
#tegla1.kerulet()
