##################################### ATIVIDADE 03 #####################################
import os
while True:
    os.system('cls')
    print('\n')
    menu = int(input('Digite o número do exercício que deseja executar:\n--> '))

    if menu == 1:
        os.system('cls')

        #Lista com as temperatudas
        temp = [25, 37, 28, 42, 31, 39, 29]
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
                    
        print(f'A menor temperatura é {menor} graus. \n')
        print(f'A maior temperatura é {maior} graus. \n')
        print(f'A média de temperatura é {soma/len(temp):.2f} \n')

    elif menu == 2:
        os.system('cls')
        valor = 0
        idade = 0

        while idade >= 0:  # Enquanto idade for maior que 0, o loop continua
            idade = int(input('Digite as idades: '))
            # Se idade for maior que 0, o contador é incrementado, e o valor é determinado pelas condicionais	
            if idade <= 2:
                valor += 0
            elif idade >= 3 and idade <= 12:
                valor += 14
            elif idade >= 65:
                valor += 18
            else:
                valor += 23
        # Saida do valor
        print()
        print(f'O valor total de passagens é: {valor:.2f}\n')

    elif menu == 3:
        os.system('cls')

        alfabetolower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        alfabetoupper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        
        # Função que criptografa a mensagem
        def criptografar(texto):
            # O texto começa vazio, e será incrementado com o valor de cada letra da lista
            texto_criptografado = ''

            # For que percorre a lista de letras
            for letra in texto:
                if letra in alfabetolower:

                    # A letra é encontrada na lista e substituida pela letra que vem três índices depois
                    posicao = alfabetolower.index(letra)
                    texto_criptografado += alfabetolower[(posicao + 3)%len(alfabetolower)]
                elif letra in alfabetoupper:
                    # Mesmo processo, porém com letras maiúsculas
                    posicao = alfabetoupper.index(letra)
                    texto_criptografado += alfabetoupper[(posicao + 3)%len(alfabetoupper)]
                else:
                    # Se não for nenhum dos dois, não é uma letra, e desse não será modificada.
                    texto_criptografado += letra
            return texto_criptografado

        # Função que descriptografa a mensagem, os processos são os mesmos de criptografar,
        # porém ao invés de adicionar 3 índices, subtrai 3 índices
        def descriptografar(texto):
            texto_descriptografado = ''
            for letra in texto:
                if letra in alfabetolower:
                    posicao = alfabetolower.index(letra)
                    texto_descriptografado += alfabetolower[(posicao - 3)%len(alfabetolower)]
                
                elif letra in alfabetoupper:
                    posicao = alfabetoupper.index(letra)
                    texto_descriptografado += alfabetoupper[(posicao - 3)%len(alfabetoupper)]
                
                else:
                    texto_descriptografado += letra
            return texto_descriptografado

        # Entradas e saídas
        escolha = int(input('Digite 1 para criptografar ou 2 para descriptografar: '))
        print('\n')
        if escolha == 1:
            texto = input('Digite o texto para criptografar: ')
            print(f'O texto criptografado é: {criptografar(texto)},\n')
        elif escolha == 2:
            texto = input('Digite o texto para descriptografar: ')
            print(f'O texto descriptografado é: {descriptografar(texto)}, \n')

    else:
        print('Opção inválida!')
        
    if input('Deseja continuar? [S/N] ').upper() == 'N':
        break