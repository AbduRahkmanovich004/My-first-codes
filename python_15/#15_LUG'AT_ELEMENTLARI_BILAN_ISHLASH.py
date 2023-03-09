#muallif:XudoyberdiyevA
#data:21/02/2023
#lugat



talaba = {
    'ism':'alijon',
    'familiya':'shamshiyev',
    'yosh':22,
    'fakultet':'matematika',
    'kurs':4
    }

print(talaba.items())


print('\n\n\n\n')

for key,qiy in talaba.items():
    print(f'kalit:{key}')
    print(f'qiymat:{qiy}\n\n')








kl = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }

for k,q in kl.items():
    print(f'{k.title()}ning telifoni {q}')


mahsulotlar = {
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }

print(mahsulotlar.keys())



print('Do\'kondagi mahsulotlar:')  #interfise sifati
for mahsulot in sorted(mahsulotlar.keys()):    #sorted metodidan foydalabdi
    print(mahsulot.title())



bozorlik=["anor","uzum","non","baliq"]
for mah in sorted(mahsulotlar):
    if mah in bozorlik:
        print(f'{mah.title()}  {mahsulotlar[mah]} s`om')





for buy in bozorlik:
    if buy not in mahsulotlar:
        print(f'iltimos dokoningizga {buy} niham olib keling')




for m in mahsulotlar.values():
    print(m)

kl = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'ali1':'iphone x',
    'vali1':'galaxy s9',
    'olim1':'mi 10 pro',
    'orif1':'nokia 3310'
    }

for k in set(kl.values()):    #set metodida ikkita bor
         print(k)                   #bolsa oshani bittasi olinadi




toys={'boll','gol','mol','shol','der','gol','mol','shol'} #bu yerda malumotr turi set
                                                            #yani nom={} shu ichida yozilsa set boladi
















