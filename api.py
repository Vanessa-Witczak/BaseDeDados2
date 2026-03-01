import requests
url = "https://api.open-meteo.com/v1/forecast?latitude=-15.60&longitude=-56.10&daily=temperature_2m_max,temperature_2m_min&timezone=America/Cuiaba"
requests.get (url)
response = requests.get(url)
dados = response.json()
print (dados)