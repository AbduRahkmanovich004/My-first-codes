
def fibonacci(n):
    sonlar=[]
    for n in range(n):
        if n==1 or n==0:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[n-1]+sonlar[n-2])
    return sonlar

print(fibonacci(10))
        

        
    
