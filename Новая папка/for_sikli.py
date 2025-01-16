ismlar=['Javohir','Elbek','Siroj','Laziz','Odil']
#for ism in ismlar:
   # print('how are you?',ism)
#print("ko'd ",len(ismlar), " marta takrorlandi")
#t_sonlar=list(range(11,100,2))
#for son in t_sonlar:
#    print(f"{son} ning kubi {son**3} ga teng")
#kinolar=[]
#print('Eng sevimli kinolaringiz qaysilar?')
#list=[1,2,3,4,5]
#for n in list:
    #kinolar.append(input(f"{n}-kinoyingizni kiriting:"))
#print(kinolar)
odamlar=[]
n=int(input('bugun nechta odam bilan uchrashdingiz:'))
list=list(range(1,n+1))
for element in list:
    odamlar.append(input(f"{element}-odamning ismini kiriting:"))
print(odamlar)
