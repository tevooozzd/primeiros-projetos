import requests
from bs4 import BeautifulSoup




print("Qual dessas cidades, você quer saber o nome?")
print(" São Paulo - 1 (GMT -3)\n California - 2 (GMT -7)\n Tokyo - 3 (GMT +9)\n Berlim - 4 (GMT  +2)")
escolha_pessoa = int(input("Digite aqui a sua escolha: "))

def horario(esc):
    if esc == 1:
        escolha = "Brasilia (GMT: -3)"
        link = "https://www.google.com/search?q=horario+em+brasilia"
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 OPR/113.0.0.0 (Edition std-2)"                 
        }
        requisição = requests.get(link, headers = header)
        site = BeautifulSoup(requisição.text, "html.parser")
        pesquisa = site.find("div", class_ ="YwPhnf")
        print(f"Sua escola foi {escolha}, e o horário é de {pesquisa.get_text()}")
     elif esc == 2:
        escolha = "California (GMT: -7)"
        link = "https://www.google.com/search?q=horario+na+california"
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 OPR/113.0.0.0 (Edition std-2)"                 
        }
        requisição = requests.get(link, headers = header)
        site = BeautifulSoup(requisição.text, "html.parser")
        pesquisa = site.find("div", class_ ="YwPhnf")
        print(f"Sua escola foi {escolha}, e o horário é de {pesquisa.get_text()}")
horario(escolha_pessoa)
