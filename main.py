import requests
import re
rep = requests.get("https://www.ldlc.com/informatique/pieces-informatique/memoire-pc/c4703/+fi62-l8+fv133-11607,11608,11610,20073,20691,20843.html?sort=1")
print (rep)

rep2 = requests.get("https://www.alternate.fr/M%C3%A9moire-vive?t=8248&s=price_asc&filter_-2=true&filter_2728=32768.0&filter_2728=65536.0&filter_2728=131072.0&filter_2728=16384.0&filter_2728=98304.0&filter_2728=49152.0&filter_2728=8192.0&filter_2728=262144.0&filter_2728=24576.0&filter_2728=196608.0&filter_2728=49512.0&filter_29829=DDR4-2133+%28PC4-17000%29&filter_29829=DDR4-2400+%28PC4-19200%29&filter_29829=DDR4-2666+%28PC4-21300%29&filter_29829=DDR4-2933+%28PC4-23400%29&filter_29829=DDR4-3000+%28PC4-24000%29&filter_29829=DDR4-3200+%28PC4-2560%29&filter_29829=DDR4-3200+%28PC4-25600%29&filter_29829=DDR4-3600+%28PC4-28800%29&filter_29829=DDR4-3733+%28PC4-29800%29&filter_29829=DDR4-4000+%28PC4-32000%29&filter_29829=DDR5-1600+%28PC5-12800%29%2C+DDR3-1600+%28PC3-12800%29&filter_29829=DDR5-4800+%28PC5-38400%29&filter_29829=DDR5-5200+%28PC5-41600%29&filter_29829=DDR5-5600+%28PC5-44800%29&filter_29829=DDR5-6000+%28PC5-48000%29&filter_29829=DDR5-6200+%28PC5-49600%29&filter_29829=DDR5-6400+%28PC5-51200%29&filter_29829=DDR5-6600+%28PC5-52800%29&filter_29829=DDR5-6800+%28PC5-54400%29&filter_29829=DDR5-7000+%28PC5-56000%29&filter_29829=DDR5-7200+%28PC5-57600%29&filter_29829=DDR5-7600+%28PC5-60800%29&filter_29829=DDR5-7800+%28PC5-62400%29&filter_29829=DDR5-8000+%28PC5-64000%29&filter_29829=DDR5-8200+%28PC5-65600%29&filter_29829=DDR5-8400+%28PC5-67200%29&filter_29829=DDR5-8600+%28PC5-68800%29&filter_29829=DDR5-8800+%28PC5-70400%29&filter_29829=DDR5-9200+%28PC5-73600%29&filter_29829=DDR5-9600+%28PC5-76800%29")
print(rep2)

from bs4 import BeautifulSoup as bs

html = rep.content

#print(html)

soup1= bs(html, "lxml")

print(soup1)

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

for product in soup1.find_all("div", class_="listing-product"):
    for prix in prix1:
      pr=prix.get_text(strip=True)
      lst2.append(pr)

lst2 = []
for script in soup1.find_all('script'):
    if script.string and 'pdtElements.forEach' in script.string:
        pattern = r'<div class="price">(\d+)€<sup>(\d+)<\/sup>'
        matches = re.findall(pattern, script.string)
        for euros, centimes in matches:
            prix_propre = f"{euros}€{centimes}"
            lst2.append(prix_propre)

lst_Ram = [f"{x} : {y}" for x, y in zip(lst1, lst2)]

for produit in lst_Ram:
    print(produit)
#print(lst2)

#prix2= soup1.find_all("sup")


#for prix in soup1.find_all("div", class_="price"):
    # Récupère tous les morceaux de texte en ignorant les espaces inutiles
 #   texte = "".join(prix.stripped_strings)   # → "1999" ou "1999€"
  #  lst2.append(texte)


lst3=[]

for prix in prix1:
    lst3.append(prix.get_text(strip=True))

#print(lst3)


#for p in soup1.find_all("div", class_="price")[:5]:
 #   print(p.prettify())
  #  print("---")

#lst_Ram=list(zip(lst1+lst2))
#lst_Ram=[f"{x} {y}" for x, y in zip(lst1, lst2)]

#print(lst_Ram)
#for titres in titres_art :
 #   for prix in prix1:
  #          print(titres.get_text(strip=True), prix.get_text(strip=True))


import pandas as pd 


df=pd.DataFrame(zip(lst1, lst2), columns= ["Article", 'Prix'])

print(df)

df.to_csv('indicateur_prix_ram.csv')
