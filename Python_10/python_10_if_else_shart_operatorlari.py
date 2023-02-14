#Muallif:XudoyberdiyevA
#Data:06/02/2023

#10-Dars if else shart operatorlari



print("10-dars /n ----------------------------------------------------------------------------1")
autos=['bmw','gm','ferrari','kia','bens','mers','audi']
for m in autos:
    if m=='bmw':    #  == Agarda bu yerda ikkita tenglik kelib qolsa TENGMI degan manoni beradi

        print(m.upper())
    else:
        print(m.title())






print("-------------------------------------------------------------------------2")
parol=input("yangi parol quying____")
ot=input("parolni kirgizing______")


if ot.title()==parol.title():
        print('succesed')
else:
        print('parol notogri')
        
        
        



print("-------------------------------------------------------------------------3")
javob=float(input("12*2=__"))
if javob==24:
    print("true")
else:
    print("false")







print("-------------------------------------------------------------------------4")
yosh=int(input("tug`ilgan yilinizni kirgazing___"))
m=2023-yosh
if m<=18:
    print(f"Sizning yoshingiz {m} da ekan krish mumkin emas! ")
else:
    print("succesed")







print("-------------------------------------------------------------------------4")
login=input("login 8 ta belgidan kop bolishi shart:___")
if len(login)<8:    print("8 ta kop belgi blishi lozim")
else:   print("succesed")
    






print("-------------------------------------------------------------------------4")
x,y=35,20
print("y dan x katta") if x>y  else  print("x dan y katta")   

