#21-dars funksiya vazifa
def boshharf(ismlar):
    '''bu matinning pbarch asoxjdfshb'''
    ismlar_q=[]
    while ismlar:
        ism=ismlar.pop().title()
        ismlar_q.append(ism)
    return ismlar_q
ooo=["azam","asad",'nodir','aziz','elyor','turgun']
aaa=ooo[:]
a=boshharf(aaa)
print(ooo)
print(a)
###################################################
def baholash(ismlar):
    baholar={}
    for m in range(len(ismlar)):
        ism=ismlar[m]
        baho=int(input(f'{ism} ismli oquvchini bahosini kirgazing:  '))
        baholar[ism]=baho
    return baholar
kidt122=["jamshid","qilichbek","asad",'dilshod']
kidt=kidt122[:]
print(baholash(kidt))
    
