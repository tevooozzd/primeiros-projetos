perguntasmatematica = {"Qual é a raiz quadrada de 144?" : "c",
        "Qual é a fórmula para calcular a área de um círculo?": "a",
            "Se um triângulo tem lados de 3 cm, 4 cm e 5 cm, ele é um triângulo?": "a",
            "Qual é o resultado de '15%' de 200?" : "b",
            "Qual é a soma dos ângulos internos de um quadrado?" : "d",
            "O que representa a hipotenusa em um triângulo retângulo?" : "a",
            "Como se chama uma sequência de números em que cada número é a soma dos dois anteriores?" : "b",

            }


opcoesmatematica  = {"Qual é a raiz quadrada de 144?" : "A) 10    B) 11    C) 12    D) 13",
            "Qual é a fórmula para calcular a área de um círculo?": "A) A=πr    B) Y=mx + b     C) A + B + C    D) P = 4l   ",
            "Se um triângulo tem lados de 3 cm, 4 cm e 5 cm, ele é um triângulo?": "A) Retângulo    B) Isóceles    C)   Escaleno    D) Quadrado",
            "Qual é o resultado de '15%' de 200?" : "A) 60    B) 30    C) 15    D) 5.75",
            "Qual é a soma dos ângulos internos de um quadrado?": " A)  40 graus   B) 50 graus   C) 180 graus  D) 360 graus ",
            "O que representa a hipotenusa em um triângulo retângulo?": " A) maior lado do triângulo    B) Nada   C) O lado do ângulo   D) O menor lado",
            "Como se chama uma sequência de números em que cada número é a soma dos dois anteriores?" : " A) Pitagoras   B) Sequência de Fibonacci C) Bhaskara  D) Algebra física",
            }
import time
acertos = 0
erros = 0
nperguntas = 0
for pergunta in perguntasmatematica:
    print(pergunta)
    print(opcoesmatematica[pergunta])

    chute = input("Qual alternativa é a resposta: ").lower()

    while chute not in ['a', 'b', 'c', 'd' ]:
        print("Essa não é uma opção!, vamos tentar novamente!")
        chute = input("Qual alternativa é a resposta: ").lower()
    
    if chute == perguntasmatematica[pergunta]:
        print("Correto!")
        acertos += 1
        nperguntas += 1
    else: 
        print("Errado!")
        erros += 1
        nperguntas += 1
    time.sleep(1)
    print(f"Essa foi a pergunta número {nperguntas}, você tem {acertos} acertos e {erros}!")
