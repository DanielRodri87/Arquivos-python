entradas = int(input())
cont = 0 
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
while cont < entradas:
    cont += 1
    palavra = str(input())
    deslocamento = int(input())
    saida = ''
    for i in palavra:
        posicao = alfabeto.index(i)
        saida += alfabeto[(posicao - deslocamento)]

    print(saida)
