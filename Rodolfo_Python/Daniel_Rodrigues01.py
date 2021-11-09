# ################# Resposta ao Exercício #################

# # 1)
# # Determinar a área e o volume de um cilindro cujas dimensões de raio e altura sejam lidas do teclado.

# # raio = float(input("Digite o raio do círculo em m²: "))
# # altura = float(input("Digite a altura do círculo em m: "))
# # print(f"A área do círculo é: {3.14 * (raio * raio)} m²\nO volume do círculo é: {3.14*(raio*raio)*altura} m³ ", )



# # 2)
# #  Calcular o perímetro e a superfície de um retângulo dadas a base e a altura. 

# # altura = float(input("Digite a altura do retângulo m: "))
# # base = float(input("Digite a base do retângulo m: "))
# # print(f"O perímetro do retângulo é: {2*(base+altura)} m\nA superfície do retângulo é de: {base*altura} m²", )



# # 3)
# # A proprietária de uma loja deseja obter o salário líquido (salário bruto deduzido dos impostos) de seus funcionários, com base no número de horas trabalhadas. O programa deve ser capaz de fazer esse cálculo a partir da quantidade de horas trabalhadas por uma pessoa, do valor (R$) da hora de trabalho e da porcentagem referente aos impostos. Ao final do cálculo, o programa deve informar os dois salários, bruto e líquido, com base nos dados de entrada.

# # horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
# # valor_hora = float(input("Digite o valor da hora trabalhada: "))
# # impostos = float(input('Digite a porcentagem de impostos (Apenas o número, sem o "%"): '))

# # salario_bruto = horas_trabalhadas * valor_hora
# # salario_liquido = salario_bruto - (salario_bruto * impostos / 100)

# # print(f"O salário bruto é: {salario_bruto:.2f}")
# # print(f"O salário líquido é: {salario_liquido:.2f}")



# ######################################################################33

# print('Banco Herbola')

# cadastrar = input('Deseja cadastrar um novo cliente? (S/N) ')
# if cadastrar == 'S':
#     nome = input('Nome: ')
#     cpf = input('CPF: ')
#     idade = input('Idade: ')
#     saldo = input('Saldo: ')
#     senha = input('Senha: ')
#     cliente = [nome, cpf, idade, saldo, senha]
#     print(cliente)
# else:
#     print('Não foi possível cadastrar o cliente.')

# login = input('Deseja fazer login? (S/N) ')
# if login == 'S':
#     cpf = input('CPF: ')
#     senha = input('Senha: ')
#     if cpf == cliente[1] and senha == cliente[4]:
#         print('Login realizado com sucesso!')
#     else:
#         print('Login inválido.')


# Menor temperatura
# maior Temperatura
# media das temperaturas

#Lista com as temperatudas
temp = [25,37,28,42,31,39]
soma = 0
for graus in range(len(temp)):
    # Criando a função para calcular a soma de todos os itens da lista
    soma += temp[graus]
    if graus == 0:
        # Aqui é atribuido o primeiro valor da lista ao maior e menor
        menor = temp[0]
        maior = temp[0]
    else:
        # Aqui é verificado se o valor atual é menor do que o anterior, e se for, atribui-se ao menor
        if temp[graus] < menor:
            menor = temp[graus]
        # Aqui é verificado se o valor atual é maior do que o anterior, e se for, atribui-se ao maior
        if temp[graus] > maior:
            maior = temp[graus]
            
print(f'A menor temperatura é {menor} graus.')
print(f'A maior temperatura é {maior} graus.')
print(f'A média de temperatura é {soma/len(temp):.2}')