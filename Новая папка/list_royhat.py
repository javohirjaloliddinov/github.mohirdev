ismlar=['Odil','Sobitxon','Muhiddin']
#print('nima gap, ',ismlar[0],' bugun futbol bormi')
#print('Assalomu aleykum, ',ismlar[1],' tuzukmisiz, bugun to\'planmaymizmi?')
#print('hello my friend, ',ismlar[2],' bo\'votimi, tuzukmisiz,')
sonlar=[45,-34,6.2,-3.5]
#print(sonlar[1]+sonlar[3])
#print(sonlar[2]-sonlar[1])
#print(sonlar[3]*sonlar[0])
#print(sonlar[2]/sonlar[3])
#print(sonlar[0]//sonlar[1])
#print(sonlar[1]%sonlar[3])
sonlar[1]=456
sonlar[3]=90.3
sonlar[2]=sonlar[2]*5
#print(sonlar)
t_shaxslar=['Amir Temur','Alisher Navoiy','Islom Karimov','Abdulla Qodiriy']
z_shaxslar=['Ilon Mask','Donald Tramp','Shavkat Mirzoyoyev','Vladimir Putin']
#print("Men tarixiy shaxslardan ",t_shaxslar.pop(2)," bilan, zamonaviy shaxslardan esa ",z_shaxslar.pop(0)," bilan suhbat qilishni istar edim.")
friends=[]
friends.append('Odil')
friends.append("Jo'ra")
friends.append('Sobitxon')
friends.append('Muhiddin')
friends.append('Muslimbek')
#print(friends)
friends.remove('Odil')
friends.remove('Muhiddin')
#print(friends)
friends.insert(0,"Jamshid")
friends.insert(2,'Ahadjon')
friends.insert(5,"Ismoil")
print(friends)
mehmonlar=[]
mehmonlar.append(friends.pop(1))

mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(2))

print(mehmonlar)
