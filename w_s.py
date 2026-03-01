import requests
from bs4 import BeautifulSoup
url = "https://apod.nasa.gov/apod/astropix.html"
response = requests.get (url)
soup = BeautifulSoup (response.text, "html.parser")

titulo = soup.find("b").text.strip()
print ("Título da Imagem de Hoje:")
print(titulo)

descricao = soup.find_all("p")[2].text.strip()
print("Descrição:")
print(descricao)

data = soup.find_all("center")[1].text.strip()
print ("Data:", data)