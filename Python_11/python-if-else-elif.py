#Muallif:XudoyberdiyevA.
#Data:13/02/2023




#print('-------------------------------------------------------------------------------------1')
#m=int(input("yoshingiz nechida"))
#    print("sizga kirish tekin")
#elif m<15:   #elif tegini hohlagancha qoshish mumkin
#    print("10000 so`m")
#else:
#    print("15000")





#if-elif-else
#print('-------------------------------------------------------------------------------------2')
#u=int(input("son kiriting"))
#if u<4:
#    narh=4
#elif u<9:
#    narh=9
#elif u<15:
#    narh=15
#else:
#    narh=20
#print(f"siz {narh}mingni tulang")





#or operatori=YOKI
#print('-------------------------------------------------------------------------------------3')
#kun=input("kunni kigazing!")
#if kun.lower()=="shanba" or kun.lower()=="yakshanba":
#    print(f"{kun.title()} dam olish kuni")
#else:
#    print(f"{kun.title()} ish kuni")





#and operatori=VA
#print('-------------------------------------------------------------------------------------4')
#kun=input("kunni kireagazing:--")
#harorat=int(input("havo harorati"))
#if kun.lower()=="shanba" or kun.lower()=="yakshanba" and harotat >= 30:
#    print("Bugun footbol o`ynaymiz")
#else:
#    print("Bugun footbol o`ynamaymiz")








#true false
#print('-------------------------------------------------------------------------------------5')
#choy=1
#ow=0
#narh=0
#if choy and ow:
#    narh=narh+10000
#elif choy or ow:
#    narh=narh+5000
#print(f"jami:{narh}")





#faqat if
#print('-------------------------------------------------------------------------------------6')
#u1=1
#u2=0
#u3=1
#u4=0
#u5=1
#u6=0
#u7=0
#narh=0
#if u1:
#    narh=narh+5000
#    print(narh)
#if u2:
#    narh=narh+5000
#    print(narh)
#if u3:
#    narh=narh+5000
#    print(narh)
#if u4:
#    narh=narh+5000
#    print(narh)
#if u5:
#    narh=narh+5000
#    print(narh)
#if u6:
#    narh=narh+5000
#    print(narh)
#if u7:
#    narh=narh+5000
#    print(narh)
#print(f"jami:{narh}")










#sonni ichidagi elementlarni tekshirish
#print('-------------------------------------------------------------------------------------7')
#ovqat=input("nma buyurtma qilasiz?")
#taomlar=["manti","osh","shashlik","go'sht","gril","cola","pepsi","somsa","perashka"]
#if ovqat.lower() in taomlar:
#    print("Buyurtma qabul qilindi")
#else:
#    print("bizda bunday taom mavjud emas!")








#print('-------------------------------------------------------------------------------------8')
#ovqat=input("nma buyurtma qilasiz?")
#taomlar=["manti","osh","shashlik","go'sht","gril","cola","pepsi","somsa","perashka"]
#if ovqat.lower() not in taomlar:
#    print("bizda bunday taom mavjud emas!")
#else:
#    print("Buyurtma qabul qilindi")

buyurtmalar=[]
narh=0
print("3 ta taom buyurtma bering!")
for m in range(3):
    buyurtmalar.append((input(f"{m+1} birinchi taomni kirgazing:__").lower()))
    print(buyurtmalar)
print(f"sizning buyurtmalaringiz {buyurtmalar}")


menu=["manti","osh","shashlik","go'sht","gril","cola","pepsi","somsa","perashka"]
for i in buyurtmalar:
    if i in menu:
        print(f"{i}=5000 so'm")
        narh=narh+5000
        print(narh)
    else:
        print(f"bizda bunday {i} mavjud emas")
print(f"\n\n\njami narh:{narh}")
    










