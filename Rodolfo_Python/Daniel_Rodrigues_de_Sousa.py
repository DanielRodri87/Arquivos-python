while True:
    import os

    menu = int(input("Escolha um número para cada questão:\n[1] Questão 1\n[2] Questão 2\n[3] Questão 3\n[4] Questão 4\n -> "))

    os.system('cls')

    if menu == 1:
        print('\n')
        print('''
        Faça um programa que leia um número indeterminado de valores inteiros, encerrando a entrada de dados
        quando for informado um valor igual a -1 (que não deve ser armazenado).
        Após esta entrada de dados, faça:
        a. Mostre a quantidade de valores que foram lidos;
        b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
        c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
        d. Exiba a soma dos valores;
        e. Exiba a média dos valores;
        f. Exiba a quantidade de valores acima da média calculada;
        g. Encerre o programa com uma mensagem.
        Obs.: coloque as letras no resultado (print) para facilitar a correção.
        ''')
        print('='*75)
        print('\n')
        lista = []
        while True:
            valor = int(input("Digite um valor: "))
            if valor != -1:
                lista.append(valor)
            else:    
                break
        
        print(f'A) a lista possuí {len(lista)} números')
        print(f'B) Os valores digitados foram: {lista}')

        for x in reversed(lista):
            print(f'C) {x}', end='\n')

        print(f'D) A soma dos valores é: {sum(lista)}')
        print(f'E) A média dos valores é: {sum(lista)/len(lista)}')

        listaAcimaMedia = []
        for x in lista:
            if x > sum(lista)/len(lista):
                listaAcimaMedia.append(x)
        
        print(f'F) A quantidade de valores acima da média é: {listaAcimaMedia}')
        print(f'G) Programa encerrado!')

    elif menu == 2:
        print('''
        \nFaça um programa que retorne as posições das palavras que começam com a letra “a” de uma lista. 
        O usuário deve digitar cinco palavras para formar a lista. O programa deve exibir as palavras inseridas
        e a posição (não o índice) das palavras que atendem ao critério informado.
        Utilize while e enumerate para percorrer a lista e gerar o resultado.\n
        ''')

        print('='*75)
        print()

        lista = []
        while len(lista) < 5:
            palavra = input('Digite uma palavra: ')
            lista.append(palavra)
        
        for i, x in enumerate(lista):
            if x[0] == 'a':
                print(f'{i} - {x}')

    elif menu == 3:
        print('''
        \nCrie um programa que lê palavras do usuário até que ele insira uma linha em branco. 
        Depois que o usuário inserir uma linha em branco, seu programa deverá exibir cada palavra
        inserida pelo usuário exatamente uma vez. As palavras devem ser exibidas em na mesma ordem
        em que foram inseridas. Por exemplo, se o usuário inserir:\n

        ''')
        print('='*75)
        print()
        lista = []
        while True:
            palavra = input('Digite uma palavra: ')
            if palavra[0] == ' ':
                break
            if palavra in lista:
                continue
            else:
                lista.append(palavra)
        for x in lista:
            print(x)
        
    elif menu == 4:
        print('''
        Um baralho padrão de cartas contém 52 cartas. Cada carta tem um dos quatro naipes junto com um valor. 
        Os naipes são normalmente espadas, copas, ouros e paus, enquanto os valores são de 2 a 10,
        Valete, Dama, Rei e Ás. Cada carta de jogo pode ser representada usando dois personagens (naipe e valor).

        O primeiro caractere é o valor da carta, com os valores de 2 a 9 sendo representados diretamente e os
        caracteres “T”, “J”, “Q”, “K” e “A” para representar os valores 10, Valete, Rainha, Rei e Ás,
        respectivamente.

        O segundo personagem é usado para representar o naipe da carta. Normalmente é uma letra:
        “S” para espadas, “H” para copas, “D” para ouros e “C” para paus.

        Crie um programa que:
        a. Usando loops criará um baralho de cartas completo, armazenando as abreviações de dois caracteres para
        todas as 52 cartas em uma lista. Retorne a lista de cartas como resultando, separando as por naipe.
        b. Embaralhe as cartas do baralho. Uma técnica que pode ser usada para embaralhar as cartas é visitar
        cada elemento da lista e trocá-lo por outro elemento aleatório. Você deve escrever seu próprio loop para
        embaralhar as cartas. Você não pode usar nenhuma função do Python para embaralhar.
        
        ''')
        print('='*75)
        print()

        def criarBaralho(baralho):

            cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
            naipes = ['S', 'H', 'D', 'C']
            for x in cartas:
                for y in naipes:
                    baralho.append(x + y)
            return baralho

        def separar(baralho):
            espadas = []
            copas = []
            ouros = []
            paus = []

            for x in baralho:
                if x[1] == 'S':
                    espadas.append(x)
                elif x[1] == 'H':
                    copas.append(x)
                elif x[1] == 'D':
                    ouros.append(x)
                elif x[1] == 'C':
                    paus.append(x)
                
            return espadas, copas, ouros, paus
        
        def embaralhar(baralho): # Não encontrei outro método de embaralhar, sem usar funções do Python
            # sem shuffle
            import random
            for i in range(len(baralho)):
                x = random.randint(0, len(baralho))
                baralho[i], baralho[x] = baralho[x], baralho[i]
            return baralho
        print()        
        print('='*75)
        print()
        
        baralho = []
        criarBaralho(baralho)
        print('='*75)
        print(f'Baralho completo: {baralho}')
        print('='*75)

        espadas, copas, ouros, paus = separar(baralho)
        print(f'Baralho separado por naipes:\nEspadas: {espadas}\nCopas: {copas}\nOuros: {ouros}\nPaus: {paus}')

        print()

        embaralhado = embaralhar(baralho)
        print(f'Baralho embaralhado:\n{embaralhado}')

    elif menu == 5:
        print('Opição inválida!')
    
    saida = input('\nDeseja sair? [S/N] ').upper()
    if saida == 'S':
        break
                    
