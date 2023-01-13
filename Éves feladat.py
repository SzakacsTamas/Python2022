import random
f=open("évek.txt","w")

napok=[31,28,31,30,31,30,31,31,30,31,30,31]


for i in range (100000):
    ev=random.randint(2003,2008)
    honap=random.randint(1,12)
    #nap=[random.randint(1,29)]
    #print(ev,"/", honap,"/",nap)
    if honap == 1 or honap==3 or honap==5 or honap==7 or honap==8 or honap==10 or honap==12:
        nap=random.randint(1,31)
        #print(ev,honap,nap2)
    elif honap==4 or honap==6 or honap==9 or honap==11:
        nap=random.randint(1,30)
    else:
        nap=random.randint(1,28)

    if nap==1 or nap==2 or nap==3 or nap==4 or nap==5 or nap==6 or nap==7 or nap==8 or nap==9:
        nap="0" + str(nap)

    if honap==1 or honap==2 or honap==3 or honap==4 or honap==5 or honap==6 or honap==7 or honap==8 or honap==9:
        honap="0" + str(honap)
    szoveg=str(ev) + "." + str(honap) +  "." + str(nap) + "\n\r" 
    #print(szoveg)

    
    

    
    f.write(szoveg)

f.close()
