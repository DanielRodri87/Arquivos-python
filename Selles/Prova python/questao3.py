num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o primeiro número: '))
num3 = int(input('Digite o primeiro número: '))

if num1 <= num2 <= num3:
    print(f'A ordem crecente é: {num1} - {num2} - {num3}')
elif num1 <= num3 <= num2:
    print(f'A ordem crecente é: {num1} - {num3} - {num2}')
elif num2 <= num1 <= num3:
    print(f'A ordem crecente é: {num2} - {num1} - {num3}')
elif num2 <= num3 <= num1:
    print(f'A ordem crecente é: {num2} - {num3} - {num1}')
elif num3 <= num1 <= num2:
    print(f'A ordem crecente é: {num3} - {num1} - {num2}')
elif num3 <= num2 <= num1:
    print(f'A ordem crecente é: {num3} - {num2} - {num1}')

#Ordem descrecente
if num1 >= num2 >= num3:
    print(f'A ordem descrecente é: {num1} - {num2} - {num3}')
elif num1 >= num3 >= num2:
    print(f'A ordem descrecente é: {num1} - {num3} - {num2}')
elif num2 >= num1 >= num3:
    print(f'A ordem descrecente é: {num2} - {num1} - {num3}')
elif num2 >= num3 >= num1:
    print(f'A ordem descrecente é: {num2} - {num3} - {num1}')
elif num3 >= num1 >= num2:
    print(f'A ordem descrecente é: {num3} - {num1} - {num2}')
elif num3 >= num2 >= num1:
    print(f'A ordem descrecente é: {num3} - {num2} - {num1}')


