#filenotfounderror
#nameerror

lista=["Bence","László","Ferenccc"]
lista.append("Martin")
try:
    print(lista[3])
except IndexError:
    print("Valami nem jó!")
else:
    print("Sikeres lefutás!")
finally:
    print("Vége!")


szam=""
while szam=="":
    try:
        szam=int(input("Kérek egy számot: "))
    except ValueError as e:
        print(e)
        print("Ez nem szám")
    except:
        print("Ismeretlen hiba")

print(szam)


