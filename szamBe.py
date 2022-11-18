#Számbekérő modul
#Többféle paraméterezéssel
#2022/11/18 Szakács Tamás

def szamBe(szoveg,tort=False, minimum=False, maximum=False):
#   print(szoveg)
#   print(tort)
#   print(minimum)

    hiba=True
    while hiba:
        try:
            if tort:
                szam=float(input(szoveg))
            else:
                szam=int(input(szoveg))
        except:
            print("H1b4 v4n")
        else:
            hiba=False
szamBe("Aggyá meg szamot: ",tort=True, minimum=10,tort=True )


#print("asdas",end="---")
#print("123456")
