import random

def rock_paper_scissors():
    jatek2="Kő, Papír, Olló"
    print("*"*len(jatek2))
    print(jatek2)
    print("*"*len(jatek2))
    print()
    while True:
        valasztas=input("Kérem a választásod (kő, papír, olló): ")
    
        lehetosegek=["kő", "papír", "olló"]
        gep=random.choice(lehetosegek)
    
        print("A gép a(z) {}-t választotta.".format(gep))
    
        if valasztas == gep:
            print("Választás ugyanaz, döntetlen.")
        elif valasztas == "kő":
            if gep == "olló":
                print("A kő üti az ollót. Nyertél! :D")
            else:
                print("A papír üti a követ. Vesztettél! :(")
        elif valasztas == "papír":
            if gep == "kő":
                print("A papír üti a követ. Nyertél! :D")
            else:
                print("Az olló üti a papírt. Vesztettél! :(")
        elif valasztas == "olló":
            if gep == "papír":
                print("Az olló üti a papírt. Nyertél! :D")
            else:
                print("A kő üti a ollót. Vesztettél! :(")
    
        ujra=input("Még egy kör? (igen/nem): ")
    
        if ujra != "igen":
            break
