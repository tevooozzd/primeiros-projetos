## - Entendendo como analisar dados do usuário 
## - Recapitulação INPUT, INT, FLOAT E STR
## - Agora utilizando análise de dados (IF, ELSE E ELSE IF)

            # Relembrando INPUT, FLOAT, INT E STR 
            #   - Caso queremos ter uma resposta do user, utilizamos o input()
input("Digite seu nome: ")
            #   - Caso queremos receber uma resposta em números utilizamos o INT E FLOAT antes do INPUT
# - Números inteiros INT
int(input("Digite sua idade: "))
# - Números decimais FLOAT
float(input("Digite o valor do produto: "))
# - Transmitir esses valores de números para string
str(variavel)


            # - Análise de dados
            #   - Vamos pegar os dados de um usuário e verificar se ele é apto a realizar determinada ação

idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
produto = float(input("O valor do produto é de: "))

if idade < 18:
    print("Você é menor de idade e não pode realizar uma compra dessa!")
elif produto > salario:
    print("Você não possui salario suficiente, sentimos muito, volte outra hora!")
else: 
    resultado = salario - produto
    print("Você pode realizar a compra e sobrará: R$" + str(resultado) + " do seu salário!")


#                                 Explicação
# 1 - Irá pegar as entradas do user
# 2 - caso seja menor que 18 anos a mensagem print1 vai aparecer, caso for maior irá continuar
# 3 - Irá pegar seu salario e o valor do produto, se o valor do produto for maior, irá retornar o print2 (pois não tem como comprar algo sem o dinheiro)
# 4 - Caso o salario for maior que o produto, ira calcular (salario - produto), e irá aparecer no print3 quanto sobrou  
