import copy 


class Myclass:
    x= 5
    def megnovel(self,mennyivel=1):
        self.x+=mennyivel
"""
print(Myclass.x)
p1=Myclass()
print(p1.x)
p2=Myclass()
p2.x=1
print(p2.x)
p1.megnovel()
p1.megnovel()
p1.megnovel()
p1.megnovel()
p1.megnovel()
p1.megnovel()
p1.megnovel()
p1.megnovel()
p1.megnovel()
p1.megnovel()
p1.megnovel()
p1.megnovel()
print(p1.x)
"""



class kutya:
    nev,fajta,agresszivitas,kor,szín=["","",0,0,""]
    def __init__(self,nev,fajta,agresszivitas,kor,szín):
        self.nev=nev
        self.fajta=fajta
        self.agresszivitas=agresszivitas
        self.kor=kor
        self.szín=szín
        
    def ugat(self):
        print("Miau-Miau")

    def koszon(self):
        print("Vau-Vau {} vagyok".format(self.nev))

    def talalkozas(self,masik):
        if self.agresszivitas > 5 or masik.agresszivitas > 5:
            #Támadás
            if self.agresszivitas >=masik.agresszivitas:
                print("Megöllek, Kutya!")
            else:
                print("Dont harap, báttya!")
        else:
            if self.agresszivitas >=masik.agresszivitas:
                print("Szevasz, Kutya!")
            else:
                print("Szia uram, báttya!")
            
                
k1=kutya("Buzi","Bernáthegyi",23,12,"RBG")
k2=kutya("Dog","Golden retriver",3,5,"Barna")


k1.ugat()
k1.koszon()
k2.koszon()


k2.talalkozas(k1)
k1.talalkozas(k2)




















































