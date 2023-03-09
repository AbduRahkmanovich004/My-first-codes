#Muallif:XudoyberdiyevA
#Date:16/02/2023


#Dictinory bilan ishlash
print("-------------------------------------------------------------------------------------------------1")
car_0={'model':'gentra',
       'rang':'qora',
       'matori':1.6,
       'yili':2023
       }
print(car_0['yili'])
print(car_0['matori'])
print(car_0['model'])
print(car_0['rang'])







eng_uz={"pen":"ruchka",
        "mouse":"sichqoncha",
        "phone":"telefon",
        "changer":"quvvatlagich",
        "bottom":"tugma",
        "lamp":"lampa"
        }










mevalar={"nok":30000,
         "anor":50000,
         "anjir":15000,
         "olma":20000,
         "shaftoli":18000
         }
print(f"Anor {mevalar['anor']} sum")
print(f"Anjir {mevalar['anjir']} sum")
print(f"Shaftoli {mevalar['shaftoli']} sum")
print(f"Nok {mevalar['nok']} sum")













talaba={"ism":"anvar",
        "fam":"ahmedov",
        "yil":2000,
        "unver":"TerDu"
        }
print(f"{talaba['ism'].title()} {talaba['fam'].title()} \
    {talaba['yil']} tug'ulgan.\
    U {talaba['unver']}da o'qiydi.")









talaba["kurs"]=1                                #bu yangi element qoshish uchun bajarilgan ish
talaba["fakultet"]="Axborot texnologiyalari"    #bu yangi element qoshish uchun bajarilgan ish
talaba["ism"]="AbuZarbek"                       #bu eski elementni ozgartirish uchun qilingan ish

talaba['kurs']=2                                #masalan talaba 2 chi kursga kochdi bunda
                                                                #shu tarzda malumot o`zgartiriladi
print(talaba)



talaba_1={}                 #bosh lugat yaratamiz

talaba_1["ism"]="jam"       #ushbu usul yordamida luga`timizga qiymat qabul qilib olamiz
talaba_1["fam"]="salimov"

print(talaba_1)






telifonlar={"Asat":"huavei Y6",
            "Nodir":"galaxy j5",
            "elyor":"galaxy A01",
            "Turg`un":"mi note 10"
            }
phone=telifonlar.get("Asat","Bunday malumot yuq")       #bu joydagi (,) dan keyyingi so`z mobodao lugarta ahtargan soz bilan
                                                        # mos tushmasa matn bolib chiqadigon soz hisoblanadi
print(phone)









































