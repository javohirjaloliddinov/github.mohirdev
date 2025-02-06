# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 23:20:32 2025

@author: User
"""

def kopaytma(*sonlar):
    """kiritilgan sonlarni ko'paytmasini hisoblaydi"""
    kop=1
    for son in sonlar:
        kop*=son
    return kop
print(kopaytma(2,89,234))




def info(ism,familya,**malumotlar):
    malumotlar['ism']=ism.title()
    malumotlar['familya']=familya.title()
    return malumotlar
print(info("javohir","JALOLIDDINOV",telefon_raqam=931375625,email='jaloliddinovjavohir445'))
    