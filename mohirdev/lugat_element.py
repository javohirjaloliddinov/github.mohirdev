phyton_lugat={
    'int':'butun son',
    'float':'o\'nli kasr son',
    'str':'matn',
    'if':'agar',
    'else':'aks holda',
    'elif':'aks holda agar',
    'lower':'pasroq',
    'upper':'teparoq',
    'for':'uchun',
    'list':'ro\'yhat',
    'tuple':'o\'zgarmas royhat'}
for kalit,qiymat in sorted(phyton_lugat.items()):
    print(f"kalit:{kalit}")
    print(f"qiymat:{qiymat}")


dav_poy={
    "o'zbekiston":"toshkent",
    "rossiya":"moskva",
    "fransiya":'parij',
    "angliya":'london',
    "aqsh":"washington",
    "hindiston":"dehli"}
for dav in sorted(dav_poy.keys()):
    print(dav.title())
for poy in sorted(dav_poy.values()):
    print(poy.title())



#davlat=input('istalgan davlatni kiriting>>>').lower()
#print(dav_poy.get(davlat,"bizda bunday malumot yo'q"))

#if davlat in dav_poy.keys():
    #print(dav_poy[davlat].title())
#else:
    print("bizda bunday malumot yo'q")




menu={
    'osh':10000,
    'shashlik':20000,
    'manti':5000,
    'lagmon':15000,
    "o'rama":12000,
    'ratatuy':50000,
    'spagetti':30000,
    "sho'rva":18000,
    "mastava":9000,
    "non":3000}
ovqatlar=[]

for n in range(1,4):
    ovqatlar.append(input(f"{n}-buyurtmani bering>>>").lower())

for ovqat in ovqatlar:
    if ovqat in menu.keys():
        print(menu[ovqat])
    else:
        print("bizda bunday taom yo'q")