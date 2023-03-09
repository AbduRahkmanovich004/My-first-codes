#24 dars song soz
#                                                            lambda argument:ifoda
import math
uzunlik=lambda pi,r:2*pi*r
print(uzunlik(math.pi,10))


###################################
product=lambda x,y:x**y
print(product(3,2))

#######################################
#def daraja(n):
#    return lambda x:x**n
#kvadrat=daraja(2)
#kub=daraja(3)
#print(kvadrat(5)+kub(2))

#map() funksiyasi
#from math import sqrt
#sonlar=list(range(11))
#ildizlari=list(map(sqrt,sonlar))
#print(sonlar,"\n",ildizlari)


sonlar=list(range(11))

def daraja2(x):
    return x*x
kvadrati=list(map(daraja2,sonlar))
print(sonlar,kvadrati)

kv=list(map(lambda x:x*x,sonlar))
print(kv)


#agar map() funksiyasi bomaganda quyidagicha yozar  edik
kiv=[]
for son in sonlar:
    kiv.append(son*son)
print(kiv)

#lamda orgali royhatlarnnii qoshish
a=[4,5,6]
b=[9,4,3]
son=list(map(lambda x,y:x+y,a,b))
print(son)


#map har qaniday malumotlar turi bilan ishlay oladi
ismlar=['olim','akbar','salim','nodir','ortiq']
k_ismlar=list(map(lambda matn:matn.upper(),ismlar))
print(k_ismlar)

#filter funksiyasi
import random as r

sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar

def juftmi(x):
    '''sonlarni juftlikka tekshiradi'''
    return x%2==0
    
a=list(filter(juftmi,kv))
print(a)

b=list(filter(lambda x:x%2==0,kv))
print(b)

import random as r

sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar
g=list(range(100))
def juftmi(x):
    """x juft bo'lsa True, aks holda False qaytaruvchu funksiya"""
    return x%2==0

juft_sonlar = list(filter(juftmi,g))
print(sonlar)
print(juft_sonlar)

mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

mevalar_b = list(filter(lambda meva:meva.startswith('q'),mevalar))
print(mevalar_b)

print(list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar)))












