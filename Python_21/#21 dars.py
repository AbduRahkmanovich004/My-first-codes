#21- dars royhat uzatish



def baholash(ismlar):
    baholar={}
    while ismlar:
        ism=ismlar.pop()
        baho=int(input(f'{ism} ismli oquvchini bahosini kirgazing:  '))
        baholar[ism]=baho
    return baholar
kidt122=["jamshid","qilichbek","asad",'dilshod']
kidt=kidt122[:]
print(baholash(kidt))
##########################################################################

        
    
