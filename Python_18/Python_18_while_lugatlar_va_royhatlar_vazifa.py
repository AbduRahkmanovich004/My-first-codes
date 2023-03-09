#print('Bu dastut mahsulotlar royhatini shakillantiradi')
#mahlar=[]
#while 1:
#    mah=input('mahsulotni kirgazing')
 #   mahlar.append(mah)
  #  if mah.lower()=='stop' or mah.lower()=='exit':
#        break
#print(mahlar,'\n\n\n')
########################################################################

#print('Bu dastur e-dokon uchun mahsulotlar lugatini yaratadi')
#mahsulotlar={}
#while 1:
 #   nom=input(f"\n\n\n{m}-chi mahsulotni nomini kirgazing!")
#    qiy=int(input("Shu mahsulotni narhini kirgazing!"))
#    mahsulotlar[nom]=qiy
#    m+=1
#    if jav == "yuq":
#        break
#for u,q in mahsulotlar.items():
#    print(f'{u}:{q}')

#########################################################################

buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}
while buyurtmalar:
    buyurtma=buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh=mahsulotlar[buyurtma]
        print(f'{buyurtma}ning narhi:{narh}')
    else:
        print(f'bizda {buyurtma} yuq')
