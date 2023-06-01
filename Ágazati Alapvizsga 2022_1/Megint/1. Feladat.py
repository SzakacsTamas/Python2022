szoveg=input("Kérj be egy szöveget: ")


while True:
    try:
        szam=int(input("Kérj be egy számot: "))
        break
    except:
        print("Ez nem egész szám.")


try:
    for i in range(szam):
        print(szoveg[szam], end="")

except:
    print("Nincs ilyen betű.")
