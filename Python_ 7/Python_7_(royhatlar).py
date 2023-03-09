#Criditor:Abzarbek Xudoyberdiyev
#Date:14/01/2023

#7-DARS ROYHATLAR
print("7-dars royhatlar".upper(),"\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

mevalar=["olma","anor","behi","nok"]
sonlar=[5200,2500,2000,5000]
aralash=["phone","mous",600,400,700]
print(mevalar,sonlar,aralash)
print(mevalar[0])#bu yerda toplamdagieementlarning tartib raqamioga qarab chiqarish hm mumkin
print(mevalar[-1].upper())#AGAR TOPLAM ELEMENLARINIOXIRIDAN CHIQARMOQCHI BO`LSALAINGOLDIGA - ISHORASI QOYILADI

mevalar[0]="dinasaur"#bu yerda toplamni istalgan elementini joyini almashtrish mumkin
print(mevalar[0])

print(mevalar)


#.append() metodi
print("\n------------------------------------------------------------------------1")
mevalar.append("Tarvuz")#to`plam.append("Qo`shmoqchi bo`lgan element nomi")
sonlar.append(5000000000)
print(sonlar)


#.insert() metodi
print("\n-------------------------------------------------------------------------2")
aralash.insert(2,"keyboard")#meod nomi.insort(qoshmoqchi bolgan joy nomi,qoshmoqchi bolgan element)
aralash.insert(2,"notepad")#izinma ketin qoshsa u turgan joyidan bitta keyyingi element bolib qoladi


#royhatdan elementlarni olib tashlash
print("\n-------------------------------------------------------------------------------3")
cars=[]
cars.append("lassetti")
cars.append("Cobalt")
cars.append("gentra")
cars.append("spark")
cars.append("nexia")
cars.append("lada")
cars.insert(0,"trekker")
cars.insert(4,"kia")
print(cars)
del cars[0]#DEMAK DEL METODI UNI OYLASHGAN ORNIGA QARB OCIRADI
del cars[0]
cars.remove("lada")#BUNDAN CHIQDI list.remove("mahulot nomi")  ORQALI ISHLAILADI
cars.remove("kia")
print(cars)

print("\n--------------------------------------------------------------------------4")
hayvonlar=['bear','wolf','cow','cet','dokey']
print(hayvonlar)
ovlangan=[hayvonlar.pop(0)]
print(ovlangan)
ovlangan1=[hayvonlar.pop()]
print(ovlangan1)

print("\n--------------------------------------------------------------------------5")
narxlar=[1000,2000,3000,-4000]
print(narxlar)
narxlar[3]=narxlar[3]+8000
print(narxlar,"\n-----------------------------------------------------------------------------")




