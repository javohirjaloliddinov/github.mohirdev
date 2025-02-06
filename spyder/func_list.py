# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 20:56:57 2025

@author: User
"""

def katta_matn(matnlar):
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].title()
    return matnlar
matnlar=['Javohir','abbos','erkin','siroj',"JAHONGIR"]
print(katta_matn(matnlar[:]))
print(matnlar)



def bahola(ismlar):
    baholar={}
    for ism in ismlar:
        ism=ism.title()
        baho=input(f"{ism}ning bahosini kiriting:")
        baholar[ism]=int(baho)
    return baholar
ismlar=['javohir',"olim","SIROJ","elBek"]
print(bahola(ismlar[:]))
print(ismlar)