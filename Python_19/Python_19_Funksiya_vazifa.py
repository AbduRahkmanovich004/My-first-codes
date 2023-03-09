##################################################################################
def y_hisobla(ism,t_yil):
    '''bu ismni aytib tugulgan yilni
hisoblash uchun funksiya'''
    print(f"{ism.title()} sizning yoshingiz {2023-t_yil}da")
print(y_hisobla.__doc__)
y_hisobla("Abuzar",2004)
##################################################################################
def kv_kub(son):
    '''bu sonni kv va kub ni hisoblovchi formula'''
    print(f'kv={son**2} kub={son**3}')
kv_kub(5)
##################################################################################
def toq_juft(son):
    """bu funksiya sonni juftr yoki toqlikka tekshiradi"""
    if son%2==0:
        print(f"{son}-juft son")
    else:
        print(f"{son}-toq son")
toq_juft(8)
toq_juft(9)
toq_juft(3)
toq_juft(1)
toq_juft(2)
toq_juft(7)
###############################################################################
def k_hisobla(x,y):
    '''katta sonni console ga chiqaqruvchi formula'''
    if x>y:
        print(x)
    elif x==y:
        print('ikkala son teng')
    else:
        print(y)
k_hisobla(967994,967994)
#############################################################################
def dar_hisobla(son,daraja):
    '''sonni darajasini hisoblaydi'''
    print(son**daraja)
dar_hisobla(23432,5)
#############################################################################
def dar_hisobla(son,daraja=2):# darajaga 2 standart shakli berildi
    '''sonni darajasini hisoblaydi'''
    print(son**daraja)
dar_hisobla(23432)
############################################################################
def bolish_alomati(son):
    '''qoldiqli bolishni aytadigan funksiya'''
    if son%2==0:
        print(f'\n\n\n{son} 2 ga qoldiqsiz bolinadi')
    else:
        print("\n\n\n error  2 ga qoldiqsiz bolinmaydi")
    if son%3==0:
        print(f'{son} 3 ga qoldiqsiz bolinadi')
    else:
        print("error 3 ga qoldiqsiz bolinmaydi")
    if son%4==0:
        print(f'{son} 4 ga qoldiqsiz bolinadi')
    else:
        print("error  4 ga qoldiqsiz bolinmaydi")
    if son%5==0:
        print(f'{son} 5 ga qoldiqsiz bolinadi')
    else:
        print("error  5 ga qoldiqsiz bolinmaydi")
    if son%6==0:
        print(f'{son} 6 ga qoldiqsiz bolinadi')
    else:
        print("error  6 ga qoldiqsiz bolinmaydi")
    if son%7==0:
        print(f'{son} 2 ga qoldiqsiz bolinadi')
    else:
        print("error  7 ga qoldiqsiz bolinmaydi")
    if son%8==0:
        print(f'{son} 8 ga qoldiqsiz bolinadi')
    else:
        print("error  8 ga qoldiqsiz bolinmaydi")
    if son%9==0:
        print(f'{son} 9 ga qoldiqsiz bolinadi')
    else:
        print("error  9 ga qoldiqsiz bolinmaydi")
    if son%10==0:
        print(f'{son} 10 ga qoldiqsiz bolinadi')
    else:
        print("error  10 ga qoldiqsiz bolinmaydi")
for m in range(1,1001):
    bolish_alomati(m)
a=input()
















