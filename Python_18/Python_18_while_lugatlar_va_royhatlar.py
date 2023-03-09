#Muallif:XudoyberdiyevA
#Data:24\02\2023
#While\lugat\royhat


#print("yaqin dostlaringizni royhatini shakillantiramiz")
#ismlar=[]
#n=1
#while 1:
#    savol=f"{n}- dostingizni ismini kirgazing!"
#    ism=input(savol)
#    ismlar.append(ism)
#    takror=input("yana ism kirgazmoqchimisiz ha/yuq:").lower()
#    if takror=="yuq":
#        break

#for i in ismlar:
#    print(i.title())


#################################################################################################################

    
    
    
#dostlar={}
#m=1
#ish=1
#while ish:
 #   ism=input(f"{m}dostingizni ismini kirgazing!")
 #   yosh=int(input("dostingizni yoshini kirgazing!"))
  #  dostlar[ism]=yosh
    #m+=1

#    jav= input("nana malumot qoshmoqchimisiz? ha\yuq")
  #  if jav == "yuq":
    #    ish=0
#for t,q in dostlar.items():

#    print( f'{t.title()}ning yoshi :{q}')    


# Royhatdan faqat bitta nom bilan atalgan elementni olib tashlash
###################################################################################################################
cars = ['lacetti','nexia','lacetti','lacetti','lacetti','toyota','nexia','lacetti','audi','malibu','nexia']
car='lacetti'
while car in cars:
    cars.remove(car)
    print(cars)




###################################################################################################################

talabalar = ['hasan', 'husan', 'olim', 'botir']
baholangan_talabalar = {}
while talabalar:
    talaba=talabalar.pop()
    baho = int(input(f"{talaba.title()}ning bahosini kiriting: "))
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba] = baho
for i,o in baholangan_talabalar.items():
    print(f'{i.title()}ning bahosi : {o}')
