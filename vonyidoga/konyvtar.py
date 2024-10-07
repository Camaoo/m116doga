konyvek=[]
with open("konyvtar.txt","r", encoding="utf-8") as forras, \
    open("konyvtar_api.txt","w", encoding="utf8") as celfile:
    forras.readline()
    for sor in forras:
        adat=sor.strip().split(",")
        konyv={"szerzo" :adat[0], "cim" :adat[1], "kiadas eve" :int(adat[2]), "isbn": adat[3], "allapot": adat[4] }
        konyvek.append(konyv)
    print(konyvek, file=celfile)
print(f"{konyvek}")