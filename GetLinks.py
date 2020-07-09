
import requests
from bs4 import BeautifulSoup as soup

dados = []
qtd_paginas = 38

for i in range(0,qtd_paginas):
    req = requests.get('https://www.wood-database.com/wood-finder/?fwp_wood_type=hardwood%2Csoftwood%2Cmonocot&fwp_paged='
                       + str(i))
    if req.status_code == 200:
        print(f'Requisição bem sucedida. {i+1}/{qtd_paginas}')
        content = req.content

    soupa = soup(content, 'html.parser')
    links = soupa.find_all(name='div', attrs={'class': 'col-md-6'})

    for item in links:
        item = str(item)
        item = item.split('><')
        dados.append(item[1])
        # print(item)
    # del content
    # del soupa
    # del links


dados_final = []
for i in dados:
    i = i.replace("a href=","")
    i = i.replace('"','')
    dados_final.append(i)
print(len(dados_final))

f = open('lista_links.txt','w+')

for i in dados_final:
    f.write(i + '\n')
