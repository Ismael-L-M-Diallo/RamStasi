### Biblios
import requests
import re
from bs4 import BeautifulSoup as bs
import pandas as pd 




### Requetes sources

rep = requests.get("https://www.ldlc.com/informatique/pieces-informatique/memoire-pc/c4703/+fi62-l8+fv133-11607,11608,11610,20073,20691,20843.html?sort=1")
print (rep)

rep2 = requests.get("https://www.alternate.fr/M%C3%A9moire-vive?t=8248&s=price_asc&filter_-2=true&filter_2728=32768.0&filter_2728=65536.0&filter_2728=131072.0&filter_2728=16384.0&filter_2728=98304.0&filter_2728=49152.0&filter_2728=8192.0&filter_2728=262144.0&filter_2728=24576.0&filter_2728=196608.0&filter_2728=49512.0&filter_29829=DDR4-2133+%28PC4-17000%29&filter_29829=DDR4-2400+%28PC4-19200%29&filter_29829=DDR4-2666+%28PC4-21300%29&filter_29829=DDR4-2933+%28PC4-23400%29&filter_29829=DDR4-3000+%28PC4-24000%29&filter_29829=DDR4-3200+%28PC4-2560%29&filter_29829=DDR4-3200+%28PC4-25600%29&filter_29829=DDR4-3600+%28PC4-28800%29&filter_29829=DDR4-3733+%28PC4-29800%29&filter_29829=DDR4-4000+%28PC4-32000%29&filter_29829=DDR5-1600+%28PC5-12800%29%2C+DDR3-1600+%28PC3-12800%29&filter_29829=DDR5-4800+%28PC5-38400%29&filter_29829=DDR5-5200+%28PC5-41600%29&filter_29829=DDR5-5600+%28PC5-44800%29&filter_29829=DDR5-6000+%28PC5-48000%29&filter_29829=DDR5-6200+%28PC5-49600%29&filter_29829=DDR5-6400+%28PC5-51200%29&filter_29829=DDR5-6600+%28PC5-52800%29&filter_29829=DDR5-6800+%28PC5-54400%29&filter_29829=DDR5-7000+%28PC5-56000%29&filter_29829=DDR5-7200+%28PC5-57600%29&filter_29829=DDR5-7600+%28PC5-60800%29&filter_29829=DDR5-7800+%28PC5-62400%29&filter_29829=DDR5-8000+%28PC5-64000%29&filter_29829=DDR5-8200+%28PC5-65600%29&filter_29829=DDR5-8400+%28PC5-67200%29&filter_29829=DDR5-8600+%28PC5-68800%29&filter_29829=DDR5-8800+%28PC5-70400%29&filter_29829=DDR5-9200+%28PC5-73600%29&filter_29829=DDR5-9600+%28PC5-76800%29")
print(rep2)

rep3=requests.get("https://www.digitec.ch/fr/s1/producttype/memoire-vive-2?so=5&filter=419%3D185105%2C3195%3D8135%7C804383%2C22035%3D722583%7C722587%7C722593%7C722555%7C722566%7C722549%7C1289353%7C1476684%7C742279%7C722574%7C1522820%7C722581%7C1299299%7C1299298%7C722591%7C722575%7C722578%7C5071371%7C1277209%7C722582%7C722590%7C722584%7C722592%7C722595")
print(rep3)






###RAM LDLC


  ##Content et HTML
html = rep.content

soup1= bs(html, "lxml")


  ##Recuperation titres
titres_art=soup1.find_all("h3", class_="title-3")

lst1=[]
  
for titres in titres_art :
  a= titres.get_text(strip=True)
  lst1.append(a)



  ##Recuperation prix
prix1= soup1.find_all("div", class_= "price")

lst2 = []
for script in soup1.find_all('script'):
    if script.string and 'pdtElements.forEach' in script.string:
        pattern = r'<div class="price">(\d+)€<sup>(\d+)<\/sup>'
        matches = re.findall(pattern, script.string)
        for euros, centimes in matches:
            prix_propre = f"{euros}.{centimes}"
            lst2.append(prix_propre)


  ##Liste fustion articles + prix
lst_Ram = [f"{x} : {y}" for x, y in zip(lst1, lst2)]

#for produit in lst_Ram:
 #   print(produit)


  ##Export en df
df=pd.DataFrame(zip(lst1, lst2), columns= ["Article", 'Prix'])

print(df)

df.to_csv('indicateur_prix_ram_ldlc.csv')





###RAM LDLC


 ##Content et HTML
 
html2=rep2.content

soup2=bs(html2, 'lxml')


  ##Recuperation prix
prix2=soup2.find_all("span", class_='price')

lst4=[]

for prix in prix2:
  c=prix.get_text(strip=True)[2:].replace(',', '.')
  lst4.append(c)

#print(lst4)


  ##Recuperation titres
lst3=[]

noms2= soup2.find_all("div", class_="product-name font-weight-bold")

for noms in noms2:
  lst3.append(noms.get_text(strip=False)[:-13])


print(lst3)


  ##Liste fustion articles + prix
lst_Ram2=[]

lst_Ram2={f"{x} : {y}" for x, y in zip(lst3, lst4)}

print(lst_Ram2)


  ##Export en df
df2= pd.DataFrame(zip(lst3, lst4), columns=["Article", "Prix "])

print(df2)

df2.to_csv("indicateur de prix de Ram Alternate.csv")







###RAM Digitec (null)

 ##Soup
html3=rep3.content
soup3= bs(html3, "lxml")

##print(soup3)

  ##Articles
titres3= soup3.find_all("div", class_="yArygEfC")

lst5=[]

for titres in titres3:
  lst5.append(int(titres.getText(strip=True)))


### FIN

  ##Merge des listes prix
lstp=lst2+lst4
print(lstp)

lstprix=[]

 ##conversion prix str a int
for prix in lstp:
  prix=float(prix)
  lstprix.append(prix)

print(lstprix)  

 ##Merge listes articles
lstart=lst1+lst3
print(lstart)


 ##Creation Dataframe de surveillances des prix de la RAM Octobre 2026
dfRam= pd.DataFrame(zip(lstart, lstprix), columns= ["Articles", "Prix"])

dfRam=dfRam.sort_values(by="Prix")
print(dfRam)

##Export csv
dfRam.to_csv("Dataframe_prix_Ram_France_2026.csv")