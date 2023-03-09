#17-dars vazifa

print('bu dastur sizning kitoblaringiz royhatini shakillantirib beradi. stop komandasi orqali toxtaydi')
fv_book=[]
n=1
while 1:
    ism=input(f'{n}-chi dostingizni kirgazing!_')
    if ism.lower()=='stop':
        break
    else:
        fv_book.append(ism)
        n+=1
print(fv_book)    

#1 usul
##########################################################################################
print('\n\n\n\nMuzeyga kirish narhini hisoblovchi dastur 1\n dasturni toxtatish uchun (stop\exit)')
n=1
while 1:
    print(f"\n\nSiz {n}-bolib foydalanyapsiz!")
    yosh=input('yoshingiz nechida')
    if yosh.lower()=='stop'or yosh.lower()=='exit':
        break
    elif  int(yosh)<=7:
        print('sizga chipta 2_000 sum')
    elif int(yosh)<=18:
        print('sizga chipta 3_000 sum')
    elif int(yosh)<65:
        print('sizga chipta 10_000 sum')   
    elif int(yosh)>=65:
        print('sizga chipta tekin')
    n+=1


#2--usuli
##########################################################################################
print('\n\n\n\nMuzeyga kirish narhini hisoblovchi dastur2 \n dasturni toxtatish uchun (stop\exit)')
n=1
sh=1
while sh:
    print(f"\n\nSiz {n}-bolib foydalanyapsiz!")
    yosh=input('yoshingiz nechida')
    if  yosh.lower()=='stop'or  yosh.lower()=='exit':
        sh=0
    elif  int(yosh)<=7:
        print('sizga chipta 2_000 sum')
    elif int(yosh)<=18:
        print('sizga chipta 3_000 sum')
    elif int(yosh)<65:
        print('sizga chipta 10_000 sum')   
    else:
        print('sizga chipta tekin')
    n+=1


#XATO YUQOTILDI
##########################################################################################
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat.title()=='Exit':
        break
    elif int(qiymat)<0:
        continue
    elif int(qiymat)>=0:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
        

















