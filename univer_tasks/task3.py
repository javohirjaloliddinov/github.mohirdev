k=int(input('k ni kiriting '))
a0=1
if k<=0:
    print('natural son kiriting')
else:
    K = 1
    while K <= k:
        a0 = K * a0 + (1 / K)

        K += 1
    print('a=', a0)


