A=float(input('A (A>1) sonini kiriting:'))
if A>1:
    N=1
    yigindi=0
    while yigindi<=A:
        N+=1
        yigindi += 1/N
    print(f"Eng kichik N: {N}, Yig'indi: {yigindi}")
else:
    print('xato')