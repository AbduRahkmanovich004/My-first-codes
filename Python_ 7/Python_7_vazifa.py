print("""AMALIYOT
Quyidagi mashqlarni bajaring:
ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 

sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 
Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 
t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting. 
Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:

friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. 
Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 
Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
\n\n\n\n\n\n\n-----------------------------------------------------------------0""")

#7-DATRS
ismlar=['Asad','Allam','Elyor']
print('salom dostim',ismlar[1])
print('qandaysan jigar',ismlar[2])
print('bojour',ismlar[0])
print('\n------------------------------------------------------------1')

#arifmetik amallar
sonlar=[9,-2,7,1.2]
a=sonlar[0]+sonlar[2]
b=sonlar[3]-sonlar[2]
c=sonlar[1]+sonlar[3]
d=sonlar[1]//sonlar[3]
print(a,b,c,d)
#ozgartirish
sonlar[1]=sonlar[1]+5
sonlar[3]=sonlar[3]+0.8
print(sonlar)

#almashtirish
print(ismlar)
ismlar[1]='Nodir'
print(ismlar)
print('\n------------------------------------------------------------------------2')


t_shahs=['bill geyts','Anvar narzullayev','ilon mask']
z_shahs=['stive jobs','albert eynshteyn','al-xorazmiy']

odam=t_shahs.pop(1)
inson=z_shahs.pop(0)
print('men',odam,' bilan suhbatlashishni hohlar \nedim tarihiy shahslardan esa ',inson,'bilan')

print(' \n--------------------------------------------------------------------3')


freands=[]
freands.append('uuuuu')
freands.append('iiiiiiiii')
freands.append('ppppp')
freands.append('tttttttt')
freands.append('rrrrrrr')
print(freands)

print(' \n--------------------------------------------------------------------4')

freands.remove('rrrrrrr')
print(freands)

print(' \n--------------------------------------------------------------------5')
print(freands)
freands.insert(0,'qqqq')
freands.insert(2,'aaaa')
freands.insert(6,'qqqq')
print(freands)
print(' \n--------------------------------------------------------------------6')
yangi_meh=[]
yangi_meh.append(freands.pop(0))
yangi_meh.append(freands.pop(1))
yangi_meh.append(freands.pop(2))
yangi_meh.append(freands.pop(3))
print(yangi_meh)
