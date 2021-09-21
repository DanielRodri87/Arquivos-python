#Feita por Daniel

numeros = []
print('Digite 5 números')
for x in range(1,6):
    numeros.append(int(input(f'Digite o {x}° Número: ')))
    
print(f'O maior número é: {max(numeros)}')
print(f'O menor número é: {min(numeros)}')