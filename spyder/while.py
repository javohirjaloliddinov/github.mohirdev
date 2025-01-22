# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 00:19:00 2025

@author: User
"""
#a=""
#while a!='stop':
    #a=input('kitoblaringizni kiriting(toxtatishni hohlesez stop deb yozing):')
    #if a!='stop':
        #print(a)
    
#print('toxtatildi')





#while True:
    #yosh=input("Yoshingizni kiriting(chiqishni hohlesez exit or quit):")
   
    #if yosh=="exit" or yosh=="quit":
        #break

    #if int(yosh)<=7:
        #narx=2000
    #elif int(yosh)<=18:
        #narx=3000
    #elif int(yosh)<=65:
        #narx=10000
    #else:
        #narx='bepul'
    #print(f"sizga {narx} so'm")
    
    
    
    
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat.title()=='Exit':
        break
    if float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
   
    
   
    
   
    
    
