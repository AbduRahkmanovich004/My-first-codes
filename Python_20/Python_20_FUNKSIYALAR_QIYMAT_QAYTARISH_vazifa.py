####################################################################
#def  dic_tuz(ismi,fam,shahar,teli='',e_maili=''):
#    mal={'ism':ismi,
#         "familyasi":fam,
#         "shahri":shahar,
 #        "tel":teli,
#         "e_mail":e_maili}
#    return mal
#v=[]
#while 1:
#    a1=input('\n\n\nismingiz nima?')
#   a2=input("familyangiz nima?")
#    a3=input('Shahringiz qayer?')
#    a4=(input('tel?'))
#    a5=input('e-mail?')
#    e=dic_tuz(a1,a2,a3,a4,a5)
#    v.append(e)
#    b= input("yana malumot qoshmoqchimisiz? yes\ no")
#    if b=="no":
#        break
#for an in v:
 #   print('\n\n\n')
#    for z,d in an.items():
#        print(f'{z}:{d}')
#print(v)
###########################################################################
#def eng_k_son(x,y,z):
#    '''sonlarning maxumumini hisoblaydi'''
#    a=max(x,y,z)
#    return(a)
#a=int(input('x: '))
#b=int(input('y: '))
#c=int(input('z: '))
#e=eng_k_son(x=a,y=b,z=c)
#print(e)
##########################################################################    
#def aylana(r):
#    '''aylanaga tegishli xossalarni aniqlaydi'''
#    a={
#        "diometri":2*r,
#        'yuzi':2*3.14*r**2,
#        'aylana_uzunligi':2*3.14*r
#        }
#    return(a)
#q=float(input("radusni kiriting?"))
#v=aylana(q)
#for s,d in v.items():
#    print(f'{s}:{d}')
##########################################################################
#def tub_son(m,n):
#    '''tub son aniqlovchi funk'''
#    royhat=[]
#    for n in range(m,n+1):
#        tub=1
#        if n==1:
#            tub=0
#        elif n==2:
#            tub=1
#        else:
#            for h in range(2,n):
#                if n%h==0:
#                    tub=0
#            if tub:
#                royhat.append(n)
#    return(royhat)
#u=int(input("oraliqni kichik tomonini kirgazing"))
#o=int(input("oraliqni katta tomonini kirgazing"))
#a=tub_son(u,o)
#print(a)
##########################################################################










