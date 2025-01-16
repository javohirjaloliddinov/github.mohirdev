m=int(input('m ni kiriting(natural son kiriting): '))
n=int(input('n ni kiriting(natural son kiriting): '))
# m va n ning E.K.U.B. ini topish
def EKUB(m,n):
    while n!=0:
        m,n=n,m%n
    return m
print(f'{m} va {n} sonlarining EKUBi: {EKUB(m,n)}')
# p va q larni topish
p=m/EKUB(m,n)
q=n/EKUB(m,n)
print(f'p={p} va q={q}')


