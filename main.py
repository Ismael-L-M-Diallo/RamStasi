import requests
rep = requests.get("https://www.ldlc.com/informatique/pieces-informatique/memoire-pc/c4703/+fi62-l8+fv133-11607,11608,11610,20073,20691,20843.html?sort=1")
print (rep)

rep2 = requests.get("https://www.alternate.fr/")
print(rep2)

from bs4 import BeautifulSoup as bs

html = rep.content

#print(html)

soup1= bs(html, "lxml")

#print(soup1)

titres_art=soup1.find_all("h3", class_="title-3")

lst1=[]
  
for titres in titres_art :
  a= titres.get_text(strip=True)
  #print(type(a))
  lst1.append(a)


#  print(titres.get_text(strip=True))

#print(lst1)

lst2=[]

prix1= soup1.find_all("div", class_= "price")

for prix in prix1:
    lst2.append(prix.get_text(strip=True))

#print(lst2)

#lst_Ram=list(zip(lst1+lst2))
lst_Ram=[f"{x} {y}" for x, y in zip(lst1, lst2)]

print(lst_Ram)
#for titres in titres_art :
 #   for prix in prix1:
  #          print(titres.get_text(strip=True), prix.get_text(strip=True))


