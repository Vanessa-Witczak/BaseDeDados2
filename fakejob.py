import requests
from bs4 import BeautifulSoup

url = 'https://realpython.github.io/fake-jobs/jobs/textile-designer-7.html'
response = requests.get(url,timeout = 20)
soup = BeautifulSoup(response.text,"html.parser")

titulo = soup.find('h1').text
print ('Título:', titulo)

empresa = soup.find('h2').text
print('Empresa:',empresa)

local_tag = soup.find('p', class_ ='location')
local = local_tag.text if local_tag else 'Local Não Encontrado'
print('Localização:', local)

data = soup.find('date')
print('Data:', data)

print('Link:', url)