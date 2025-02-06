# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:21:46 2025

@author: User
"""
new_list=[]

sozlar=['salom','hdefgeeeeff','alilk.']
for soz in sozlar:
    if soz==sozlar[-1]:
        soz=soz
    else:
        if len(soz)%2==1:
            soz=soz.replace(soz[len(soz)//2],'')
    new_list.append(soz)
print(new_list)
