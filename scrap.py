import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/the-requiem-red_995/index.html"
response = requests.get(url,timeout = 20)
soup = BeautifulSoup(response.text,"html.parser")

titulo = soup.find('h1').text
print ('Título:', titulo)

preco = soup.find('p', class_ = 'price_color').text
print('Preço:', preco)

estoque = soup.find('p', class_ = 'instock availability').text.strip()
print('Estoque:',estoque)

descricao = soup.find('div', id = 'product_description').find_next('p').text
print('Descrição:',descricao)