#muallif:XudoyberdiyevA
#data:26\02\2023
#19-dars Funksiyalar
def saloom_ber():    #funksiya yaratamiz
    '''saloom beruvchi funksiya'''
    print('asalomu alaykum')
saloom_ber()# bu yerda funksiyani chaqirdik
##################################################################################################
def salom_ber(ism):
    """Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya""" #uchtalik qavis ichida DOCSTRING yani discriptioni yozildi
    print(f"Assalomu alaykum, hurmatli {ism.title()}!")
salom_ber('nodir')
salom_ber('asad')
    #DOCSTRING
##################################################################################################
print(print.__doc__) #DOCSTRINGni shu tariqa bilish mnumkin
print(range.__doc__)
print(list.__doc__)


##################################################################################################
def toliq_ism(ism, familiya):#2 talik parametrdan foydalanamiz
    """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
    print(f"\n\n\n\nFoydalanuvchi ismi: {ism.title()}\n"
          f"Foydalanuvchi familiyasi: {familiya.title()}")
toliq_ism("Abu Zarbek","Xudoyberdiyev") #bunda ism va familyani joyini o`zgartirib qoyishsa funksiya notogri ishlydi
toliq_ism(familiya='Xudoyberdiyev',ism="Abu Zarbek")#Parametrni elon qilgan holda yozilsa joy almashishining farqi yuq

#######################################################################################################
def yosh_hisobla(ism, tugilgan_yil):
    """Foydalanuvchi yoshini hisoblaydigan dastur"""
    print(f"{ism.title()} {2023-tugilgan_yil} yoshda")
print(yosh_hisobla.__doc__)
yosh_hisobla("abuzar",2004)
yosh_hisobla(tugilgan_yil=2004,ism="abuzar") #ikkalasi teng kuchli hisoblanadi




#STANDART HOLATNI ISHLATISH
#####################################################################################################
def yoshni_hisobla(tugilgan_yil, joriy_yil=2023): #BU YERDA joriy yilni kkregazish shart emas chunki standart qiymat kirgazilgan
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
yoshni_hisobla(2004)#bunda  standard qiymat qabul qilgani uchun joriy yilni kirgazish sharmas
yoshni_hisobla(2004,2023)#kirgazilgan taqdirda ham notog`ri deb qaralmaydi



