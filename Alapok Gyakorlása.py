gyumolcsok=["alma","szőlő","körte","barac","sárkány","izé"]

print("Ennyi gyümölcs van: {}".format(len(gyumolcsok)))


index=gyumolcsok.index("barac")
gyumolcsok[index]+="k"
print(gyumolcsok)

print("rövid gyümölcsök")
for i in range(len(gyumolcsok)):
    if len(gyumolcsok[i]) < 5:
        print(gyumolcsok[i])
#for i in gyumolcsok:
#    print(i)
