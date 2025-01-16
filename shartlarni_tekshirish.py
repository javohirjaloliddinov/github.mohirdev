#a=float(input('juft son kiriting: '))
#if a%2==0:
    #print('rahmat')
#else:
    #print('bu juft son emas')


#yosh=int(input('yoshingiz nechchida: '))
#if yosh<=4 or yosh>=60:
    #narh='bepul'
#elif yosh<=18:
    #narh=10000
#if 18<yosh<60:
    #narh=20000
#print(f"chipta narxi {narh}")


#a=float(input('1-sonni kiriting: '))
#b=float(input('2-sonni kiriting: '))
#if a==b:
    #print('sonlar teng!')
#if a>b:
    #print('1-son 2-sidan katta')
#if a<b:
    #print('2-son 1-sidan katta')


#mahsulotlar=['gurunch','grechka','grutka','baliq','go\'sht','olma','banan','sut','tvorog','gerkules','non']

#savat=input('kamida 5 ta mahsulot nomini yozing(vergul bilan yozing)>>>').split(",")
#print(savat)
#for mahsulot in savat:
    #if mahsulot in mahsulotlar:
        #print(f"{mahsulot} do'konimizda bor")
    #else:
        #print(f"{mahsulot} do'konimizda yo'q")



bor_mahsulotlar=[]
yoq_mahsulotlar=[]
mahsulotlar=['gurunch','grechka','grutka','baliq','go\'sht','olma','banan','sut','tvorog','gerkules','non']

savat=input('kamida 5 ta mahsulot nomini yozing(vergul bilan yozing)>>>').split(",")
print(savat)
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
         yoq_mahsulotlar.append(mahsulot)
print(bor_mahsulotlar)
print(yoq_mahsulotlar)
if yoq_mahsulotlar:
    print("do'konimizda quyidagi narsalar yo'q")
    for mahsulot in yoq_mahsulotlar:
        print(mahsulot)
else:
    print("siz so'ragan barcha mahsulotlar do'konimizda bor")



#foydalanuvchilar=['Javohir','Siroj','Elbek','Laziz','Jahongir']
#foydalanuvchi=input('yangi login kiriting!>>>')
#if foydalanuvchi.title() in foydalanuvchilar:
    #print("Login band, yangi login tanlang!")
#else:
    #print(f"xush kelibsiz,{foydalanuvchi.title()}")


#son=int(input('biror butun son kiriting: '))
#for n in range(2,11):
    #if son%n==0:
        #print(n)