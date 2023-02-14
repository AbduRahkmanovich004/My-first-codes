#08_PYTHON_DARSLARI___RO'YXAT_BILAN_ISHLASH_O'ZGARMAS_RO'YXATLAR

print("08_Python_Darslari___Ro'yxat_bilan_ishlash_O'zgarmas_ro'yxatlar".upper())




#ro`yhatdagielementlarni tartiblangan holda chiqarish
print("============================================================1")
cars=["bmw",'genaral motors',"kea","bugatti","ferrari"]
print(cars)
cars.sort()
print(cars)#!!! ASIL ROYHAT HAM TAHLANGAN HOLATGA O`TADI


#royhatni alfabetga teskari ravishda chiqaradai ____.sort(reverse=True) metodi yordamida
print("\n\n============================================================2")
print(cars)
cars.sort(reverse=True)
print(cars)#!!! ASIL ROYHAT HAM TAHLANGAN HOLATGA O`TADI



#asil royhat ozgarmagan holda royhat elementlarini konsolega tartiblangan elementlarni chiqarish
print("\n\n============================================================3")
sonlar=[1, -1, 8.2, 9, -14]
print(sonlar)
print(sorted(sonlar))#bu toplam elementlarini


#asil royhat ozgarmagan holda royhat elementlarini konsolega teskari tartiblangan elementlarni chiqarish
print("\n\n============================================================4")
print(sonlar)
print(sorted(sonlar,reverse=True))




#royhatni tartiblamasdan turib uni shu holatiga chiqarish ____.reverse() metodi
print("\n\n============================================================5")
family=["mom","dad","grenddad","grendmom","bnrather","siste"]
print(family)
family.reverse()
print(family)


#len() lenth-uzunlik  Funksiyasi royhat elementlarini hajmini(yani elementlari sonini) korsatadi
print("\n\n============================================================6")
uzunlik=len(family)
print(uzunlik)#demak family elementi ichida 6 ta element bor





#   _______=list(range(__,__)) bu funksiya malum bir oraliqdaqi tartiblangqan
#   sonlarni royhat shakliga otkazadi
print("\n\n============================================================7")
m_toplam=list(range(1,11))
print(m_toplam)




#royhat elementlarining min,max,sum larini toipish
print("\n\n============================================================8")
k=list(range(20,41))
minum=min(k)
maxum=max(k)
yigindisi=sum(k)
print(minum,maxum,yigindisi)





#royhatdan element kesish
print("\n\n============================================================9")
qiymatlar=list(range(2,100,4))
print(qiymatlar)
c=qiymatlar[2:5]
print('3 elementdan 5 elemengacha kesilgan sonlar--------',c,"jami elemenlar:",len(qiymatlar))






#nusxa kochirish
print("\n\n============================================================10")
mashina=['kea', 'genaral motors', 'ferrari', 'bugatti', 'bmw']
#    mashinalar=bickele
#    ^^^^^^^^^^^^^^^^^^bu belgilash hato hisoblanadi bu bir toplamhga 2 ta nom berishdiir
#    bunda ikkita nom berilsa ham bir toplam  ustida amallar bajariladi
velo=mashina[2:]        #----|
transport=mashina[:2]   #-------bu kesishga misol bola oladi
airport=mashina[1:5]    #----|
mark=mashina[:]
print(velo,"----------",airport,"-----------",transport,'---------',mark)










#TUPLES ozgarmas royhat
print("\n\n============================================================11")
royhat=tuple(range(0,20))
#	agar sanoq 0 dan boshlansa uni cars=list(range(10)) kabi yozsa ham buladi

print(royhat)
print(type(royhat))
#      [ ] ning joyiga() qavslar ishlatilsa bu ozgarmas toplam boladi
#       bunday toplamga hech qandaysiga edit  qilib bolmayadi
#       !!! Aga mobodo zarurat boib qolsa uni list ga otkazish lozim

royhat=list(royhat)
royhat.remove(10)
print(type(royhat))
print(royhat)
royhat=tuple(royhat)
print(type(royhat))
#       shu  amalllar bajariladi



