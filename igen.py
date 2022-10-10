beSzam=0

while beSzam<2 or beSzam>5:
    beSzam=int(input("Adj meg egy számot 2 és 5 között:"))


autok=[]
for i in range(0,beSzam):
    print(i)
    autok.append(input("Kérek a(z) "+str(i +1)+" . autó márkát:"))

print(autok)

szo="Almafa"
mgh=["ö","ü","ó","o","p","ő","ú","l","j","í","d"]
if szo[0] in mgh:
    print("az")
else:
    print("a")
