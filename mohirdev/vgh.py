x=float(input('x ni kiriting:'))
N=int(input('N ni kiriting(butun son kiriting):'))
if x==0 and N==0:
    print('bu holatda x 0 ni qabul qila olmaydi')
if N>0 and N//2==N/2:
    print((x**(N/2))**2)
if N>0 and N%2==1:
    print(x*x**(N-1))
if N<0:
    print(1/(x**(-N)))      
