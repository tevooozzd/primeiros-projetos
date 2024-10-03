perguntas = {"Qual é a capital do Brasil" : "a",
            "Qual é o maior planeta do sistema solar?": "b",
            "Quem pintou a Mona Lisa?": "c",
            "Qual é o continente conhecido como 'berço da civilização'?" : "c"
            }


opcoes  = {"Qual é a capital do Brasil" : "A) Brasília B) São Paulo C) Rio de Janeiro",
            "Qual é o maior planeta do sistema solar?": "A) Terra B) Júpiter C)Marte",
            "Quem pintou a Mona Lisa?": "A) Vincent van Gogh B) Pablo Picasso C) Leonardo da Vinci",
            "Qual é o continente conhecido como 'berço da civilização'?" : "A) América B) Ásia C) África"
            }
import time
acertos = 0
erros = 0
nperguntas = 0
for pergunta in perguntas:
    print(pergunta)
    print(opcoes[pergunta])

    chute = input("Qual alternativa é a resposta: ").lower()

    while chute not in ['a', 'b', 'c']:
        print("Essa não é uma opção!, vamos tentar novamente!")
    
    if chute == perguntas[pergunta]:
        print("Correto!")
        acertos += 1
        nperguntas += 1
    else: 
        print("Errado!")
        erros += 1
        nperguntas += 1
    time.sleep(1)
    print(f"Essa foi a pergunta número {nperguntas}, você tem {acertos} acertos e {erros}!")
