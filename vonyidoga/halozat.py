halozatok=[]
with open('hálózat.txt', 'r', encoding='utf-8') as forras, \
    open('hálózat_api.txt','w',encoding='utf-8') as celfile:
    for sor in forras:
        adat=sor.strip().split(',')
        halozat={'kliens'   :adat[0], \
                 'adat'    :adat[1], \
                 }
        halozatok.append(halozat)
    print(halozatok , file=celfile)
print(f'{halozatok}') 