while True:
    print('SEJA BEM-VINDO AO BANCO DANESCO! \n')
    print('Para iniciar, digite o seu nome: ')
    nome = input()
    print('Bem-vindo, ' + nome + '! \n')

    print(f'{nome} você já é cliente Danesco? \n [S] para Sim, e [N] para não')
    resposta = input()

    if resposta == 'N':
        print('=========IRÁ COMEÇAR AS ETAPAS PARA A CRIAÇÃO DE SUA CONTA=====')
        print('Para começar, digite seu CPF: ')
        cpf = input()
        print('Digite sua nova senha: ')
        senha = input()
        
        arquivo = open('Danesco.txt', 'a')
        arquivo.write(f'{nome} {cpf} {senha} \n')
        arquivo.close()
        print('Sua conta foi criada com sucesso!')

    elif resposta == 'S':
        print('=========IRÁ COMEÇAR AS ETAPAS PARA A LOGIN=====')
        print('Digite seu CPF: ')
        cpf = input()
        print('Digite sua senha: ')
        senha = input()
        
        arquivo = open('Danesco.txt', 'r')
        for linha in arquivo:
            dados = linha.split()
            if dados[1] == cpf and dados[2] == senha:
                print('Login realizado com sucesso!')
                
                menu = input('Digite [1] para saque, [2] para depósito, [3] para transferência, [4] para sair: ')
                if menu == '1':
                    print('Digite o valor do saque: ')
                    valor = int(input())
                    print('Seu saque foi realizado com sucesso!')
                    print('Seu saldo atual é de: ' + str(valor))
                    arquivo = open('Danesco.txt', 'r')
                    for linha in arquivo:
                        dados = linha.split()
                        if dados[1] == cpf:
                            print('Seu saldo atual é de: ' - str(valor))
                            arquivo = open('Danesco.txt', 'w')
                            arquivo.write(f'{nome} {cpf} {senha} {valor} \n')
                            arquivo.close()
                            break
                elif menu == '2':
                    print('Digite o valor do depósito: ')
                    valor = int(input())
                    arquivo = open('Danesco.txt', 'r')
                    for linha in arquivo:
                        dados = linha.split()
                        if dados[1] == cpf:
                            print('Seu saldo atual é de: ' + str(valor))
                            arquivo = open('Danesco.txt', 'w')
                            arquivo.write(f'{nome} {cpf} {senha} {valor} \n')
                            arquivo.close()
                            break
                elif menu == '3':
                    print('Digite o valor da transferência: ')
                    valor = int(input())
                    print('Seu transferência foi realizado com sucesso!')
                    print('Seu saldo atual é de: ' + str(valor))
                    arquivo = open('Danesco.txt', 'r')
                    for linha in arquivo:
                        dados = linha.split()
                        if dados[1] == cpf:
                            print('Seu saldo atual é de: ' - str(valor))
                            arquivo = open('Danesco.txt', 'w')
                            arquivo.write(f'{nome} {cpf} {senha} {valor} \n')
                            arquivo.close()
                            break
                elif menu == '4':
                    print('Saindo...')
                    break
                
        else:
            print('CPF ou senha incorretos!')
        arquivo.close()
    else:
        print('Opção inválida!')
    print('Deseja continuar? \n [S] para Sim, e [N] para não')
    saida = input()
    if saida == 'N':
        break