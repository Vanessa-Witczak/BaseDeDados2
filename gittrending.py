import requests
from bs4 import BeautifulSoup

url = "https://github.com/trending"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

repos = soup.find_all("article", class_="Box-row")

for repo in repos:

    titulo = repo.h2.text.strip().replace("\n", "").replace(" ", "")

    descricao_tag = repo.find("p")
    descricao = descricao_tag.text.strip() if descricao_tag else "Sem descrição"

    link = "https://github.com" + repo.h2.a["href"]

    print("Repositório:", titulo)
    print("Descrição:", descricao)
    print("Link:", link)
    print("-" * 40)