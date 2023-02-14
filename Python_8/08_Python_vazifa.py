#   8-vazifalari


print("""AMALIYOT
O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
Ro'yxatning uzunligini konsolga chiqaring
sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
Asl ro'yxatni qaytadan konsolga chiqaring
reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
Ro'yxatdagi elementlar sonini hisoblang
Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
nonushta degan yangi ro'yxatga taomlardan nusxa oling
Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
JAVOBLAR""")








print("============================================================1")
davlatlar=('Uzb','Rus','USA','Turk','BAA','China','Frn','India')
print(davlatlar)


print("============================================================2")
print("royhatda",len(davlatlar),"ta davlat bor")





print("============================================================3")
print(sorted(davlatlar))



print("============================================================4")
print(sorted(davlatlar,reverse=True))



print("============================================================5")
print(davlatlar)




print("============================================================6")
cars=list(range(2,90,4))
print(cars)
cars.reverse()
print(cars)



print("============================================================7")
print(davlatlar)
davlatlar=list(davlatlar)
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)





print("============================================================8")
juft_sonlar=list(range(120,1201,2))
print("juft sonlar :\t",juft_sonlar)




print("============================================================9")
a=sum(juft_sonlar)
print("120 dan1200GACHA SONLAR YIGINDISI:\t",a)





print("============================================================10")
e_katta_s=max(juft_sonlar)
e_kichik_s=min(juft_sonlar)
print("ayirmalari:",e_katta_s-e_kichik_s,"\t",e_kichik_s-e_katta_s)





print("============================================================11")
print(len(juft_sonlar))




print("============================================================12")
boshidan=juft_sonlar[:20]
ortasidan=juft_sonlar[260:280]
oxiridan=juft_sonlar[521:]
print("boshidagi 20 talik:\t",boshidan,"ortasidan 20 talik:\t",ortasidan,"oxiridan 20 talik:\t",oxiridan)






print("============================================================13")
taomlar=("samsa","osh","manti","gosht","shashlik")
nonushta=list(taomlar[:])
nonushta.remove("osh")
del nonushta[2]
nonushta.append("ko`k choy")
nonushta.insert(0,"shedraleta")
print(taomlar,"\n",nonushta)
nonushta=tuple(nonushta)
print(type(nonushta),"da ozgartirib bolmaydi")




