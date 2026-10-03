#  RAMSTASI

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

**Monitoring du prix de la RAM en France | Price Monitoring of RAM in french market .**
<img width="807" height="579" alt="image" src="https://github.com/user-attachments/assets/ebc96513-49df-4654-97cd-ca8db69e4820" />


##  Contexte métier

Analyse du prix moyen de la RAM sur le marche francais pour :
- Surveillance du marche
- Détection des baisses de prix

Analysis of the median RAM price on the french market :

 -Monitoring of the market evolution
 -Detection of prices drop

 
##  Dataset
- **Sources** : LDLC / Alternate / Digitec

##  Stack technique | Technical libraries

Scrapping : Requests + BeautifulSoup
Data : Pandas + CSV 


##  Fonctionnalités | Functionalities
- Recuperation des donnees sur les plateformes e-commerce de revente de RAM
- Tri et Nettoyage
- Generation des CSV

- Data harvest
- Sorting and cleaning
- CSV generation


##  Résultats | Results

- CSV affichant depuis deux sites fiables une fourchette de prix de ce qui disponible en ce qui concerne les memoires vives.
- CSV files displaying from two viable websites price range of available RAM




##  Installation locale | Installation Guide

- Clone:
git clone https://github.com/Ismael-L-M-Diallo/RamStasi
cd RamStasi/

- Environnement virtuel | Virtual Environment:
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

 - Dependances:
 pip install pandas
 pip install lxml
 pip install bs4

## Structure projet

├── main.py                 # Dashboard principal
├── CSV/                   # Données brutes
│   ├── merged_hourly_regional.csv
│   └── merged_daily_regional.csv
├── README.md


## Contributing

Fork → Modifs → Pull Request

## Licence

MIT License - Apache 2.0

## Remerciements | Special Thanks

 -Les sites susmentionnes
 -Mentionned websites
