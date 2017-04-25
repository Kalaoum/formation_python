datas = ("chaud","froid","tempéré","glacial","brûlant")

file = "c:\\tmp\\temperatures.txt"

with open(file,"w") as fic:
    for mot in datas:
        print(fic.write("%s\n" % mot))

datas_en = ("hot","cold","moderate","icy","ardent")
with open(file,"a") as fic:
    for mot in datas_en:
        print(fic.write("%s\n" % mot))

print("Controle :")
with open(file, "r") as fic:
    print(fic.read())