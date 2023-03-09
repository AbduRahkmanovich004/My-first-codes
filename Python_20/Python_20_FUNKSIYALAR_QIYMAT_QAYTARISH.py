#muallif:XudoyberdiyevA
#Data:26\02\2023
# dars_20_FUNKSIYALAR_QIYMAT_QAYTARISH
#############################################################################################################################
def toliq_ism_yasa(ism, familiya):
    """Toliq isma qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism                                                # qiymat qaytarish uchun return operatorini ishlatamiz
talaba1 = toliq_ism_yasa('olim','hakimov')
talaba2 = toliq_ism_yasa('hakim','olimov')
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
print(f'{talaba1.title()} darsga kechikib keldi')


#IXTIYORIY ELEMENT
###############################################################################################################
def toliq_ism_yasa(ism, familiya, otasining_ismi=''):   #BU YERDA PARAMETR_NOMI="" KORINISHIDA KOD YOZSAK IXTIYORIY ELEMENT BOLADI
    """Toliq isma qaytaruvchi funksiya"""
    if otasining_ismi: # otasining_ismi mavjudligini tekshiramiz
        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
    else:
        toliq_ism = f"{ism} {familiya}"
    return toliq_ism.title()
alaba1 = toliq_ism_yasa('olim','hakimov') #otasining_ismi kiritilmadi
talaba2 = toliq_ism_yasa('hakim','olimov','abrorovich')
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
##############################################################################################################################
def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto
avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)#NARXI KIRGAZILMAGAN
avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
avtolar = [avto1, avto2] #LUGATNI ROYHATGA JOYLAYMIZ
print('Onlayn bozordagi mavjud avtomashinalar:')
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "Noma'lum"
    print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")
#######################################################################################################################
def range_yasa(min,max,qadam=1):
    '''range funksiyasi'''
    sonlar=[]
    while min<max:
        sonlar.append(min)
        min+=qadam
    return sonlar
print(range_yasa(1,5000,13))


#tsikli bilan
####################################################################################################################
def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto

print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
while True:
    print("\nQuyidagi ma'lumotlarni kiriting")
    kompaniya=input(" Ishlab chiqaruvchi: ")
    model=input("Modeli: ")
    rangi=input("Rangi: ")
    korobka=input("Korobka: ")
    yili=input("Ishlab chiqarilgan yili: ")
    narhi=input("Narhi: ")
    
    #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
    #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
    # Yana avto qo'shish-qo'shmaslikni so'raymiz
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob=='no':
        break
for k,q in avtolar[0].items():
    print(f'{k} : {q}')













