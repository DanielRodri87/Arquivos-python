
valid = soma = cont = maior = menor = 0
num = []
while True :
    x = int(input('Digite um número:'))
    if x != -1:
        num.append(x)
        cont += 1
        soma += x
    else:   
        break
        
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(num)