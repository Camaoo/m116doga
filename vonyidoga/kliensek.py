kliensek=[]
with open('kliensek.txt', 'r', encoding='utf-8') as forras, \
    open('kliensek_api.txt','w',encoding='utf-8') as celfile:
    for sor in forras:
        adat=sor.strip().split(',')
        halozat={'kliens'   :adat[0], \
                 'ipv4'    :adat[1], \
                 'ipv6' :adat[2], \
                 'interface' :adat[3], \
                 'subnetmask' :adat[4]
                 }
        kliensek.append(halozat)
    print(kliensek , file=celfile)
print(f'{kliensek}') 