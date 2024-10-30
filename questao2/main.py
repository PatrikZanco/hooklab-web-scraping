import json

"""
Considere que você tenha feito o web scraping de uma API que contém o resultado de uma
pesquisa em um e-commerce. A resposta da API está em formato json no arquivo
api_response.json enviado junto ao desafio.
O arquivo possui inúmeras informações utilizadas pelo site para mostrar os resultados, mas
seu trabalho é extrair uma lista com as ofertas resultantes da pesquisa. O objetivo é extrair
os atributos principais das ofertas.
Exemplo de pesquisa: https://www.climario.com.br/geladeira?_q=geladeira&map=ft
List of:
- offer_link -> link da oferta
- image_link -> link da imagem do produto
- price -> preço da oferta
- title -> título da oferta
"""

with open('data/api_response.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# print(data.keys())

info = data["Product:sp-33854.items({\"filter\":\"ALL\"}).0"]
print(info)


