print(list(range(1,51)))


def oraliq(a,b):
    sonlar=[]
    while a<b:
        sonlar.append(a)
        a+=1
    return sonlar
print(oraliq(1,51))




print(list(range(1,51,3)))


def oraliq(a,b,c=None):
    sonlar=[]
    if c:
        while a<b:
            sonlar.append(a)
            a+=c
    else:
        while a<b:
           sonlar.append(a)
           a+=1
    return sonlar
        
print(oraliq(1,51,3))
print(oraliq(1,100,5))
print(oraliq(1,43))







def tub_son(a,b):
    tub_sonlar=[]
    
    for n in range(a,b+1):
        tub=True
        if n==1:
            tub=False
        if n==2:
            tub=True
        else:
            for x in range(2,n):
                if(n%x==0):
                    tub = False
        if tub:
            tub_sonlar.append(n)
        
    return tub_sonlar

print(tub_son(2,999))



def fibonachchi(n):
    sonlar=[]
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x-2]+sonlar[x-1])
    return sonlar
print(fibonachchi(12))
        












