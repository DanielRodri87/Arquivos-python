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
print(f'A média de temperatura é {soma/len(temp):.2f}')