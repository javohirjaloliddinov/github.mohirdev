buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
           'tyil':810,
           'vyil':870,
           'tjoy':'Buxoro'
           }

qodiriy = {'ism':'Abdulla Qodiriy',
           'tyil':1894,
           'vyil':1938,
           'tjoy':'Toshkent'
           }

vohidov = {'ism':'Erkin Vohidov',
           'tyil':1936,
           'vyil':2016,
           'tjoy':"Farg'ona"
           }

navoiy = {'ism':'Alisher Navoiy',
           'tyil':1441,
           'vyil':1501,
           'tjoy':"Xirot"}
adabiyotshunoslar=[buxoriy,qodiriy,vohidov,navoiy]

for shoir in adabiyotshunoslar:
    print(f"{shoir['ism']} {shoir['tyil']}-yili "
          f"{shoir['tjoy']} shahrida tug'ilgan. "
          f"U {shoir['vyil']}-yili o'lgan.")



buxoriy['asarlari']=["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]
qodiriy['asarlari']=["O'tkan kunlar","Mehrobdan Chayon",'Obid ketmon']
vohidov['asarlari']=["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
navoiy['asarlari']=["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
print(adabiyotshunoslar)
for shoir in adabiyotshunoslar:
    print(f"{shoir['ism']} manashu asarlarni yozgan:")
    for asar in shoir['asarlari']:
        print(asar.title())



kinolar = {
    'ali':['Terminator','Rambo','Titanic'],
    'vali':['Tenet','Inception','Interstellar'],
    'hasan':['Abdullajon','Bomba','Shaytanat'],
    'husan':['Mahallada duv-duv gap','John Wick']
    }
for kalit,qiymat in kinolar.items():
    print(f"{kalit.title()} shu kinolarni yaxshi ko'radi:")
    for kino in qiymat:
        print(kino)




davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
               'maydon':17_098_246,
               'aholi':144_000_000,
               'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
    }
for kalit,qiymat in davlatlar.items():
    print(f"{kalit.title()}ning poytaxti {qiymat['poytaxt'].title()}. "
          f"Maydoni {qiymat['maydon']} km kv. "
          f"Aholisi {qiymat['aholi']} ta. "
          f"Pul birligi {qiymat['pul birligi']}.")





davlatlar = {
    "o'zbekiston": {'poytaxt': "toshkent",
                    'maydon': 448978,
                    'aholi': 33_000_000,
                    'pul birligi': "so'm"
                    },
    "rossiya": {'poytaxt': "moskva",
                'maydon': 17_098_246,
                'aholi': 144_000_000,
                'pul birligi': "rubl"
                },
    "aqsh": {'poytaxt': "vashington",
             'maydon': 9_631_418,
             'aholi': 327_000_000,
             'pul birligi': "dollar"},
    "malayziya": {'poytaxt': "kuala-lumpur",
                  'maydon': 329750,
                  'aholi': 25_000_000,
                  'pul birligi': "rinngit"}
}


davlat=input('davlatni kiriting>>>').lower()

if davlat in davlatlar.keys():
    print(f"{davlat.title()}ning poytaxti {davlatlar[davlat]['poytaxt'].title()}. "
          f"Maydoni {davlatlar[davlat]['maydon']} km kv. "
          f"Aholisi {davlatlar[davlat]['aholi']} ta. "
          f"Pul birligi {davlatlar[davlat]['pul birligi']}.")

else:
    print("bizda bu davlat haqida ma'lumot yo'q")

