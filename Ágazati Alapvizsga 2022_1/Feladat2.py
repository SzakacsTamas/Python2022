def haromszog():
    vissza=[]
    for i in range(3):
        szam=""
        while szam =="":
            try:
                szam=int(input("Kérek egy szamot: "))
            except:
                print("Ez nem egy szám!")

        vissza.append(szam)

    return vissza
