#Muallif:XudoyberdiyevA
#Data:24\02\2023
#while   input



#ism=str(input("ismingiz nima?"))
#ism = input("Ismingiz nima? ")
#savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
#yosh = input(savol)


#ism = input("Ismingiz nima? ")
#savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
#yosh = input(savol)
#yosh = int(yosh) # yosh ni butun songa o'tkazamiz
#height = input("Bo'yingiz necha metr? ")
#height = float(height) # bo'yni o'nlik songa o'tkazamiz

###########################################################################

son=1
while son<100:
    print(son,end=" ")
    son += 1    # son=son+1 ga teng
print("dastur tugadi")


#MANTIQ BILAN
##############################################################################
#print("bu dastur kiritgan sonni kvadratini hisoblovchi dastur")
#savol="Istalgan sonni kirgazing."
#savol+=' dasturdan chiqish uchun exit deb yozing:'
#qiymat=""
#while qiymat != 'exit':
#    qiymat=input(savol)
#    if qiymat != 'exit':
#        print(float(qiymat)**2)

#print("Dastur tugadi")



# True False
###############################################################################
#print("bu dastur kiritgan sonni kvadratini hisoblovchi dastur")
#savol="Istalgan sonni kirgazing."
#savol+=' dasturdan chiqish uchun exit deb yozing:'
#ishora=True
#while ishora:
#    qiymat=input(savol)
#    if qiymat != 'exit':
#        print(float(qiymat)**2)
#    else:
#        ishora=False

#print("Dastur tugadi")


#BREAK bilan
#####################################################################################
#print("bu dastur kiritgan sonni kvadratini hisoblovchi dastur")
#savol="Istalgan sonni kirgazing."
#savol+=' dasturdan chiqish uchun exit deb yozing:'
#while 1:
#    qiymat=input(savol)
#    if qiymat != 'exit':
#        print(float(qiymat)**2)
#    else:
#        break

#print("Dastur tugadi")




#####################################################################################
sonlar=list(range(1,11))
for son in sonlar:
    if son == 5: #bu yerda break buyrugi dasturni oxirigacha ishlashni cheklab qoydi
        break
    print(f"{son}ning kvadrati: {son**2}")



#xuddi tepadagi kabi sikel yozamiz Continue bilan davom etish jarayoni korsatamiz.
#####################################################################################
sonlar=list(range(1,11))
for son in sonlar:
    if son == 5: #bu yerda continue buyrugi dasturdagi 5 sonini kv sini hisoblamay otib ketadi
        continue      
    print(f"{son}ning kvadrati: {son**2}")



#TOQ yoki JUFT sonni hisoblaydirgon dastur
######################################################################################

num=0
while num<10:
    num+=1
    if num%2!=0:  #bu yerda aksincha quyganimizda == toq sonlar bolardi
        continue
    else:
        print(num)


num=0
while num<10:
    num+=1
    if num%2==0:  #bu yerda aksincha quyganimizda != juft sonlar bolardi
        continue
    else:
        print(num)
#BU KOD VIRUS YANI MANTIQDA XATO KETGAN
#############################################################################################################
num=0
while num>=0:
    num+=1
    if num%2==0:  #bu yerda aksincha quyganimizda != juft sonlar bolardi
        continue
    else:
        print(num)





    
