# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:53:38 2025

@author: User
"""
#1-task
mahsulotlar=[]
n=1
while True:
    mahsulot=input(f'{n}-mahsulotni yozing(toxtatmoqchi bolsayiz exit yozing):')
    if mahsulot=='exit':
        break
    else:
        mahsulotlar.append(mahsulot)
    n+=1
print(mahsulotlar)



#2-task
narxlar={}
n=1
while True:
    mahsulot=input(f"{n}-mahsulotni kiriting(toxtatmoqchi bo'lsayiz exit yozing):")
    if mahsulot=='exit':
        break
    else:
        narx=input(f"{mahsulot} ning narxini kiriting:")
        narxlar[mahsulot]=float(narx)
    n+=1
print(narxlar)


#1 va 2 tasklarni ham pastagini ham qo'shsak 3-task
for mahsulot in mahsulotlar:
    if mahsulot in narxlar.keys():
        print(f"{mahsulot}ning narxi {narxlar[mahsulot]}")
    else:
        print("Bizda bu mahsulot yo'q")