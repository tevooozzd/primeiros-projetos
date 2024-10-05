import requests
from bs4 import BeautifulSoup

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 OPR/113.0.0.0 (Edition std-2)"
    }

link = 'https://www.google.com/search?q=horario+em+brasilia&client=opera-g'
requisicao = requests.get(link, headers = header)
site = BeautifulSoup(requisicao.text, "html.parser")

pesquisa = site.find("div", class_ = "gsrt vk_bk FzvWSb YwPhnf")
resul = pesquisa.get_text()
print(f"O horário atual de Brasília(GMT -3) é {resul}")
