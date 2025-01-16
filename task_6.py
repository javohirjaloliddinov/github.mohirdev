list1= input('ro\'yhatni kiriting(vergul bilan kiriting):'). split(",")
print(list1)
k=int(input('k ni kiriting(natural son kiriting):'))

if 1<=k<len(list1):
    for n in range(1,k+1):
        del list1[0]
        list1.append(0)
    print(list1)
else:
    print("k ni to'g'ri kiriting")
             