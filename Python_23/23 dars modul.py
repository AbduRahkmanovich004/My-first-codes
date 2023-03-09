#https://docs.python.org/3/py-modindex.html


#modul chaqirish
import modul
avto1 = modul.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
modul.info_print(avto1)



#modulni biron nom bilan nomlash
import modul as papka
avto1 = papka.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
papka.info_print(avto1)



#funksiyalarni ozini kodimizga inport qilish
from modul import avto_info, info_print
avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
info_print(avto1)


#o`zlashtirilgan funksiyaga nom berish
from modul import avto_info as ainfo, info_print as iprint
avto1 = ainfo("GM", "Malibu", "Qora", "avtomat", 2020,40000)
iprint(avto1)


#bu yerda modul ichidagi barcha funksiyalarni chaqiramiz
from modul import *
avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
info_print(avto1)

#pythondagi kodlar moduli
import math
x=400
print(math.sqrt(x))
print(pow(5,5))
from math import pi
print(pi)
print(math.log2(8))
print(math.log10(100))
import random as r # random modulini r deb chaqirayapmiz

son = r.randint(0,100) # 0 va 100 oralig'ida tasodifiy son
print(son)
x = list(range(11))
print(x)
r.shuffle(x)
print(x)
x = list(range(0,51,5))
print(x)
print(r.choice(x))




