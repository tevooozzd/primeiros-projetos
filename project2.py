# - Entendendo o uso do input, float, int e src
# - Input utilizamos para recerbemos entrada do user



            #INPUT
nome = input("Digite seu nome: ")
print(nome) # Output: Digite seu nome: (entrada do user, (exemplo 'Ana'))
            # Output: Ana



            #FLOAT, INT E STC
# - Caso queremos que o úsuario coloque números, utilizamos o FLOAT E INT
# - FLOAT serve para números decimais
# - Já int serve para números inteiros
# - STC, serve para converter NÚMEROS ( FLOAT E INT) para STRING
idade = int(input('Digite sua idade: ')) # - Não tem como uma pessoa ter anos e meio, por isso utilizamos o INT
preço = float(input("O produto x custa: ")) # - Um item/objeto pode valer (X Valor) e com isso pode utilizar centavos, por isso usamos o FLOAT
salario = float(input("Digite seu salário:  ")) # - Uma pessoa pode receber em valor decimal, como em centavos por isso usamos o FLOAT


        # - Caso os números nao sejam convertidos em STR, você recebe uma mensagem de erro

print("Sua idade é de: " + str(idade)) # Output: "Sua idade é de: x"
print("O produto custa : " + str(preço)) # Output: "O produto custa: y"
print("Seu salário é de : "  + str(salario)) # Output: "Seu salariio é de: z"
