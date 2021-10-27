################# Resposta ao Exercício #################

# 1)
# Determinar a área e o volume de um cilindro cujas dimensões de raio e altura sejam lidas do teclado.

# raio = float(input("Digite o raio do círculo em m²: "))
# altura = float(input("Digite a altura do círculo em m: "))
# print(f"A área do círculo é: {3.14 * (raio * raio):.2} m²\nO voulme do círculo é: {3.14*(raio*raio)*altura:.3} m³ ", )



# 2)
#  Calcular o perímetro e a superfície de um retângulo dadas a base e a altura. 

# altura = float(input("Digite a altura do retângulo m: "))
# base = float(input("Digite a base do retângulo m: "))
# print(f"O perímetro do retângulo é: {2*(base+altura)} m\nA área do retângulo é: {base*altura} m²", )



# 3)
# A proprietária de uma loja deseja obter o salário líquido (salário bruto deduzido dos impostos) de seus funcionários, com base no número de horas trabalhadas. O programa deve ser capaz de fazer esse cálculo a partir da quantidade de horas trabalhadas por uma pessoa, do valor (R$) da hora de trabalho e da porcentagem referente aos impostos. Ao final do cálculo, o programa deve informar os dois salários, bruto e líquido, com base nos dados de entrada.

horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
valor_hora = float(input("Digite o valor da hora trabalhada: "))
impostos = float(input('Digite a porcentagem de impostos (Apenas o número, sem o "%"): '))

salario_bruto = horas_trabalhadas * valor_hora
salario_liquido = salario_bruto - (salario_bruto * impostos / 100)

print(f"O salário bruto é: {salario_bruto:.2f}")
print(f"O salário líquido é: {salario_liquido:.2f}")
