#muallif: Xudoyberdiyev A
#Data: 23/02/2023

#python_16_nesting_vazifa
####################################################################################################################
allomalar={
    'ism_0':{'ism':'Abu abdulloh Ibn muhammad ismoil',
        'tugulgan_k':810,
        'vatani':'Buxoro',
        'umri':60
        },
    'ism_1':{'ism':'Abdulla Qodiriy',
        'tugulgan_k':1894,
        'vatani':'Toshkent',
        'umri':44
        },
    'ism_2':{'ism':'Erkin Vohidov',
        'tugulgan_k':1936,
        'vatani':'Toshkent',
        'umri':80
        },
    'ism_3':{'ism':'Alisher Navoiy',
        'tugulgan_k':1441,
        'vatani':'Hirotr',
        'umri':60
        }
    }
for ismi in allomalar.values():
    print(f"\n{ismi['ism']} {ismi['tugulgan_k']}-yil {ismi['vatani']}da tugulgan. ",end="")
    print(f"u {ismi['umri']} yil umr ko`rgan.",end='')

###############################################################################################################################

buxoriy = {'name':'Abu Abdulloh Muhammad ibn Ismoil',
           'tyil':810,
           'vyil':870,
           'tjoy':'Buxoro',
           'asarlar':["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]
           }

qodiriy = {'name':'Abdulla Qodiriy',
           'tyil':1894,
           'vyil':1938,
           'tjoy':'Toshkent',
           'asarlar':["O'tkan kunlar","Mehrobdan Chayon",'Obid ketmon']
           }

vohidov = {'name':'Erkin Vohidov',
           'tyil':1936,
           'vyil':2016,
           'tjoy':"Farg'ona",
           'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
           }

navoiy = {'name':'Alisher Navoiy',
           'tyil':1441,
           'vyil':1501,
           'tjoy':"Xirot",
           'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
           }


shahslar=[buxoriy,qodiriy,vohidov,navoiy]

for m in shahslar:
    print(f'\n\n{m["name"]} ning yozgan asarlari:')
    for q in m['asarlar']:
        print(q)

##############################################################################################################################

kinolar = {
    'ali':['Terminator','Rambo','Titanic'],
    'vali':['Tenet','Inception','Interstellar'],
    'hasan':['Abdullajon','Bomba','Shaytanat'],
    'husan':['Mahallada duv-duv gap','John Wick']
    }

for m,q in kinolar.items():
    print(f'\n\n\n{m.title()}ning sevimli filmlari:')
    for w in q:
        print("\n",w)


##############################################################################################################################

davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
    }

for kk,qq in davlatlar.items():
    print(f'\n\n\n\n\n{kk.title()} davlat haqida qisqacha:')
    for jj in qq:
        print(f'\n{jj.title()}:{qq[jj]}')

##############################################################################################################################


davlatlar = {
    "uzbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"
                   },
    "ispanya":{'poytaxt':"Madrid",
                   'maydon':329750,
                   'aholi':45_000_000,
                   'pul birligi':"yevro"}
    }

#dav=input("Qaysi davlat haqida ma'lumot olmoqchisiz?").lower()

#for mal in davlatlar:
#    if dav in davlatlar:
#        print(f'{dav.title()} haqida qisqacha malumotlar:')
#        for ii in mal.keys():
#            print(f'{ii}:{mal[ii]}')
#    else:
#        print(f'Bizning bazada {dav.title()} haqida malumot yuq')



davlat = input('Davlat nomini kiriting: ').lower()

if davlat in davlatlar:
    for uu in davlatlar[davlat]:
        print(f'\n\n{uu.title()}:{davlatlar[davlat][uu]}')
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")
            
            
        
        







