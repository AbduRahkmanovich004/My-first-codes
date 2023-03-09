#22-dars *args **kwdrds
def summa(r,t,*sonlar):
    y=sum(sonlar)
    return y
a=summa(565,6161,16516,6161,111,2,222,21,15,1,55,15,)
print(a)
##################################################################
def avtoinfo(rangi,model,**malumotlar):
    malumotlar["model"]=model
    malumotlar['rangi']=rangi
    return malumotlar
auto1=avtoinfo( "qizil","lasetti",narhi=1500 , karobka="auto")
auto2=avtoinfo("yashil","matiz",narhi=1000)
print(auto1,'\n',auto2)
