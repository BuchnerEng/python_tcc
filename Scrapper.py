"""
O objetivo deste código é fazer scrap dos dados das páginas do site https://www.wood-database.com

https://www.wood-database.com/bois-de-rose/

"""
from HTMLStrip import strip_tags
import pandas as pd
import requests
from bs4 import BeautifulSoup as soup

req = requests.get('https://www.wood-database.com/fijian-kauri/')

if req.status_code == 200:
    print('Requisição bem sucedida.')
    content = req.content

cont_soup = soup(content, 'html.parser')
table = cont_soup.find_all(name='p')

dados = []

for item in table:
    item = strip_tags(str(item))
    dados.append(item)
    print(item)
    if 'Color/Appearance' in item:
        break
dados.pop()
print(dados)
