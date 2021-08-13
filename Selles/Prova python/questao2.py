num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
num3 = float(input('Digite outro número: '))

maior = 0               
menor = 0              
print()

#descobrindo o maior:
if num1 > num2 and num1 > num3:
    print(f'O maior número é: {num1}')
    maior = num1
elif num2 > num1 and num2 > num3:
    print(f'O maior número é: {num2}')
    maior = num2
elif num3 > num1 and num3 > num2:
    print(f'O maior número é: {num3}')
    maior = num3

#descobrindo o menor:
if num1 < num2 and num1 < num3:
    print(f'O menor é: {num1}')
    menor = num1
elif num2 < num1 and num2 < num3:
    print(f'O menor é: {num2}')
    menor = num2
elif num3 < num1 and num3 < num2:
    print(f'O menor é: {num3}')
    menor = num3

#Descobrindo o do meio:
if maior > num1 > menor:
    print(f'O número do meio é: {num1}')
elif maior > num2 > menor:
    print(f'O número do meio é: {num2}')
elif maior > num3 > menor:
    print(f'O número do meio é: {num3}')
