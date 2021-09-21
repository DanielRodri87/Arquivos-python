numeros = []

numbers = input("Insira 3 números separadas por espaço: ").split()

for x in range(3):
    while True: 
        try:
            numeros.append(int(numbers[x]))
            break
        except ValueError:
            numeros.append(float(numbers[x]))
            break
n1 = numeros[0]
n2 = numeros[1]
n3 = numeros[2]

result_soma = n1 + n2 + n3
if result_soma % 2 == 0:
    par_or_impar = "par"
else:
    par_or_impar = "ímpar"
if result_soma > 0:
    positivo = True
if type(result_soma) == int:
    tipo = "inteiro"
else:
    tipo = "decimal"

print(f"A soma dos números é {result_soma}, é um número {par_or_impar}, do tipo {tipo}.")