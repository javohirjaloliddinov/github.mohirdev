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

