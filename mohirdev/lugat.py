otam={'ismi':"Jamoliddin",'tugilgan_yili':1981,'shahri':"uchqo'rg'on"}
print(f"Otamning ismi {otam['ismi']},{otam['tugilgan_yili']}-yilda, {otam['shahri']} shahrida tug'ilgan.")
taomlar={
    'Jahongir':'osh',
    'Dilnoza':'manti',
    'Jobir':'lagmon',
    'Nodirabegim':'shashlik',
    'Malika':'mastava'}
print(f"Jahongirnig sevimli taomi {taomlar['Jahongir']}.")
print(f"Jobirning sevimli taomi {taomlar['Jobir']}.")
print(f"Malikaning sevimli taomi {taomlar['Malika']}.")
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
print(phyton_lugat)


kalit=input('biror soz kiriting>>>')
#print(phyton_lugat.get(kalit.lower(),'bunday soz mavjud emas'))


if kalit in phyton_lugat:
    print(phyton_lugat[kalit])
else:
    print('bunday soz mavjud emas')
