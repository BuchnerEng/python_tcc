"""
O objetivo deste código é fazer scrap dos dados das páginas do site https://www.wood-database.com

https://www.wood-database.com/bois-de-rose/

"""
from HTMLStrip import strip_tags
import pandas as pd
import requests
from bs4 import BeautifulSoup as soup
from openpyxl import load_workbook

chaves_valida = ['Common Name(s)',
                 'Scientific Name',
                 'Distribution',
                 'Average Dried Weight',
                 'Specific Gravity (Basic, 12% MC)',
                 'Janka Hardness', 'Modulus of Rupture',
                 'Elastic Modulus',
                 'Crushing Strength',
                 'Tree Size',
                 'Shrinkage']

df_base = pd.DataFrame(chaves_valida, index=chaves_valida)

arquivo = open('lista_links.txt', 'r')

for id, linha in enumerate(arquivo):
    req = requests.get(linha)

    if req.status_code == 200:
        print(f'Requisição bem sucedida.{id}')
        content = req.content
    try:
        cont_soup = soup(content, 'html.parser')
        table = cont_soup.find_all(name='p')

        dados = []
        conferir = ['Radial:', 'Tangential:', 'Volumetric:', 'T/R Ratio:']

        for item in table:
            item = strip_tags(str(item))
            item = item.replace('\xa0', '')
            if item and '>' not in item and 'More images' not in item:
                dados.append(item)
            if 'Color/Appearance' in item:
                break
        dados.pop()

        # print(dados)

        for indice, linha in enumerate(dados):
            if ":" not in linha:
                concatenado = ''.join(dados[indice - 1:indice + 1])
                dados.pop(indice)
                dados.pop(indice - 1)
                dados.append(concatenado)
            elif 'Volumetric:' in linha and 'Shrinkage' not in linha:
                concatenado = ''.join(dados[indice - 1:indice + 1])
                dados.pop(indice)
                dados.pop(indice - 1)
                dados.append(concatenado)
            elif '*Strength' in linha:
                dados.pop(indice)

        # for x in dados:
        #     print(x)
        #
        # print(len(dados))

        dados_tratados = {}
        for objeto in dados:
            objeto = objeto.split(':')
            dados_tratados[objeto[0]] = ';'.join(objeto[1:])

        for key in dados_tratados:
            if key not in chaves_valida:
                dados_tratados.pop(key)
            # print(key, '###', dados_tratados[key])

        df_base[id] = pd.DataFrame.from_dict(dados_tratados, orient='index')
    except:
        print(f'Erro de conteúdo, linha {id}')

print(df_base)

work_book = load_workbook('Resultado.xlsx')
new_sheet = pd.ExcelWriter('Resultado.xlsx')
new_sheet.book = work_book
df_base.to_excel(new_sheet, sheet_name='Resultado_Final')
new_sheet.save()
new_sheet.close()
