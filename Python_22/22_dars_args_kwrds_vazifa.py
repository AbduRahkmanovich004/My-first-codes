#22 dars moslashuvchan
###########################################################
def kv(*sonlar):
    son=1
    for n in sonlar:
        son=n*son
    return son
ee=kv(154,485,48,48,48,4,84,8,4,84,8,4,8,48,4,848,4184)
print(ee)
###########################################################
def tinfo(ismi,fam,**malumotlar):
    malumotlar["fam"]=fam
    malumotlar['ismi']=ismi
    return malumotlar
talaba1=tinfo( "khudoyberdiyev","abzarbek",auditoriya="axborot texnologiyalari", yonalish="kidt")
print(talaba1)
