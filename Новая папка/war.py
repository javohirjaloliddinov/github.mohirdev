a=int(input('a ni kiriting:'))
b=int(input('b ni kiriting:'))

    
def Ekub(a,b):
    while b!=0:
        a,b=b,a%b
    return a
print(Ekub(a,b))
c=Ekub(a,b)
p=a//c
q=b//c
print(f"{a}\{b}={p}\{q}")


