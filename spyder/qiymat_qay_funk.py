def info(ism,familya,t_yil,t_joy,t_raq=None,email=None):
    lugat={'ism':ism.title(),
          'familya':familya.title(),
          't_yil':t_yil,
          'yoshi':2025-t_yil,
          't_joy':t_joy,
          't_raq':t_raq,
          'email':email}
    return lugat

ism=input("ismingizni kiriting:")
familya=input("familyangizni kiriting:")
t_yil=int(input("tug'ilgan yilingizni kiriting:"))
t_joy=input("tug'ilgan joyingizni kiriting:")
t_raq=int(input("telefon raqamingizni kiriting:"))
email=input("emailingizni kiriting:")
print(info(ism,familya,t_yil,t_joy,t_raq,email))
          
         
            
         
            
         
            
infoes=[]
def info(ism,familya,t_yil,t_joy,t_raq=None,email=None):
    lugat={'ism':ism.title(),
          'familya':familya.title(),
          't_yil':t_yil,
          'yoshi':2025-t_yil,
          't_joy':t_joy,
          't_raq':t_raq,
          'email':email}
    return lugat
while True:
    ism=input("ismni kiriting:")
    familya=input("familyani kiriting:")
    t_yil=int(input("tug'ilgan yilni kiriting:"))
    t_joy=input("tug'ilgan joyni kiriting:")
    t_raq=int(input("telefon raqamni kiriting:"))
    email=input("emailni kiriting:")
    infoes.append(info(ism,familya,t_yil,t_joy,t_raq,email))
    javob=input("yana info qo'shishni hohlaysanmi:ha\\yoq:")
    if javob=='yoq':
        break
for info in infoes:
    print(f"{info['ism']} {info['familya']} {info['t_yil']}-yili {info['t_joy']}da tug'ilgan "
          f"telefon raqami:{info['t_raq']}, email manzili:{info['email']}")
    








def kattasi(a,b,c):
    kat=a
    if b>=a:
        kat=b
    if c>=kat:
        kat=c
    return kat
print(kattasi(2,4,1))
print(kattasi(4,4,4))
print(kattasi(34,23,99))


def radius(r):
    info={'radius':r,
          'diametr':2*r,
          'l':2*3.14*r,
          's':3.14*(r**2)}
    return info
print(radius(3))






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
        
















