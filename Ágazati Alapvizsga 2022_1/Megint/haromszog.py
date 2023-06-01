def haromszog():
    try:
        oldal1=int(input("Kérd be az 1. számot"))
    except:
        print("Csak számot fogadok el!")

    try:
        oldal2=int(input("Kérd be a 2. számot"))
    except:
        print("Csak számot fogadok el!")


    try:
        oldal3=int(input("Kérd be 3. számot"))
    except:
        print("Csak számot fogadok el!")

    return[oldal1,oldal2,oldal3]



haromszog()
