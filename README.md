# python_tcc
O código GetLinks itera sobre o site e pega todos os links das madeiras, salva um link por linha no arquivo de texto lista_links.txt

O código Scrapper itera sobre um link, pega as informações da tabela até Shrinkage e salva em uma lista python.

Futuramente o Scrapper irá:
  1. Iterar sobre o arquivo lista_links.txt para realizar a captura de informação de cada madeira.
  2. Tratar melhor os textos, no momento só retirei as tags html.
  3. Separar os dados de maneira lógica para um banco.
  4. Criar o DataFrame pandas seguindo a lógica anterior.
  5. Informar ao usuário qual número da iteração está sendo realizada.
  6. Exportar o DataFrame (possivelmente para um csv ou xlsx)
  
  No momento os códigos não estão documentados, nem muito organizados, farei isso depois.
