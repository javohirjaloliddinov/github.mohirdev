# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 10:28:56 2025

@author: User
"""

def t_yil_his(ism,yosh):
    """Tugilgan yilizni hisoblovchi funksiya"""
    print(f"{ism.title()} siz {2025-yosh}-yilsiz")
t_yil_his('javohir',18)
t_yil_his('jahongir',14)



def kv_kub_beradi(son):
    """kiritgan sonizni kv va kub ini hisoblab beradi"""
    print(son**2)
    print(son**3)
kv_kub_beradi(7)
kv_kub_beradi(12)


def j_t_aniqlaydi(son):
    """Kiritgan sonizni juft yoki toqligini aniqlaydi"""
    if son<0:
        print('musbat butun son kiriting')
    elif son%2==0:
        print(f"{son} juft son")
    elif son%2==1:
        print(f"{son} toq son")
j_t_aniqlaydi(-9)
j_t_aniqlaydi(0)
j_t_aniqlaydi(16)
j_t_aniqlaydi(7)



def kattasini_chiqar(a,b):
    """2 sonni kattasini chiqaradi"""
    if a>b:
        print(a)
    elif a<b:
        print(b)
    else:
        print("sonlar teng")
kattasini_chiqar(4,8)
kattasini_chiqar(45,12)
kattasini_chiqar(-9,-7)
kattasini_chiqar(5,5)




def daraja(x,y=2):
    """x ni y ingchi darajasini hisoblaydi"""
    print(f"{x} ning {y}-darajasi {x**y} ga teng")
daraja(6)
daraja(4,3)
daraja(4,-15)


def qoldiqsiz_bol(son):
    for n in range(2,11):
        if son%n==False:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")
qoldiqsiz_bol(45)
qoldiqsiz_bol(34)

















