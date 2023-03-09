def tub_son(m,n):
    '''tub son aniqlovchi funk'''
    royhat=[]
    for n in range(m,n+1):
        tub=1
        if n==1:
            tub=0
        elif n==2:
            tub=True
        else:
            for h in range(2,n):
                if n%h==0:
                    tub=0
            if tub:
                royhat.append(n)
    return(royhat)
print("___________tub sonni hisoblovchi dastur___________")
u=int(input("oraliqni kichik tomonini kirgazing"))
o=int(input("oraliqni katta tomonini kirgazing"))
a=tub_son(u,o)
print(a)
o=input()
