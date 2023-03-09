kl = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'alk':'sdsd',
    'fafsfa':'sfasf',
    'fsgsg':'rwgfg',
    'dsdss':'dsvvsdv',
    'ysdvsdvds':'sdvsdv'
    }

for m in sorted(kl.keys()):
    print(m.title())



dav={
    'afina':'Gretsiya',
    'zagreb':'Xorvatiya',
    'budapesht':'Vengriya',
    'vatikan':'Vatikan',
    'kiyev':'Ukraina',
    'tiraspol':'Dnestrboʻyi Moldova Respublikasi'
    }
print('Dunyo davlatlari:')
for davlat in sorted(dav):
    print(davlat.upper())

print('\nDavlatlarning poytaxtlari')
for poytaxt in sorted(dav.values()):
    print(poytaxt.title())



davlat=input("qaysi  davlatni poytahtini bilmoqchisiz?").lower()
for h in dav:
    if h==davlat:
        print(f'{h.title()}ning poytahti {dav[h]}')





menu={
    "somsa":10000,
    'manti':3000,
    'shorva':5000,
    'grill':50000,
    'gosht':80000,
    'lavash':20000,
    'pita':25000,
    'osh':28000
    }
print('3 ta taom kirgazing')
buy=[]
for m in range(3):
    buy.append(input(f'{m+1}-ta`om:').lower())
i=0
for taom in buy:
    if taom in menu:
        print(f"\n{taom} {menu[taom]} so`m")
        i+=menu[taom]
    else:
        print(f"\nKechirasiz. Bizda {taom} yuq")
print(f"\n\n\n\njami:{i}")






