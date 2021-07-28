while True:
    print('---------------------------------------------------------------------------------------------')
    print ('')
    print ('SEJA BEM-VINDO(A) AO MENU, ESCOLHA A OPÇÃO QUE LHE FOR ÚTIL!')
    print ('')
    print('---------------------------------------------------------------------------------------------')

    print ('''
    [1] Soma
    [2] Vezes
    [3] Divisão
    [4] Banco
    [5] Média
    [6] Salário
    ''')
    opcao = int(input('Escolha uma opção:  '))    

    if opcao == 1 :
        s1 = float(input('Digite o primeiro número: '))
        s2 = float(input('Digite o segundo número: '))
        s = s1 + s2
        print('Resultado é: {}' .format(s))

    if opcao == 2 :
        m1 = float(input('Digite o primeiro número: '))
        m2 = float(input('Digite o segundo número: '))
        mult = m1 * m2
        print('Resultado é: {}' .format(mult))

    if opcao == 3 :
        d1 = float(input('Digite o primeiro número: '))
        d2 = float(input('Digite o segundo número: '))
        div = d1 / d2
        print('Resultado é: {}' .format(div))

    if opcao == 4 :
        #interação inicial
        print('')
        print('')
        print('============================================================')
        print('SEJA BEM-VINDO AO BANCO DANESCO')
        print('============================================================')
        print('')
        print('')

        numeroconta = input('Digite o número de sua conta:')
        senha = input('Digite sua senha:')
        conta = int(input ("Valor para sacar:"))

        #saldo inicial e variável
        saldo = 21631
        resultante = saldo - conta

        #Operações de saque
        if conta <= 2000:
            print('')
            print('ESTAMOS QUASE TERMINANDO:')
            print('')
            print ('O VALOR DO SAQUE: {} ESTÁ DISPONIVEL, \n NÃO SAIA SEM RETIRAR O CARTÃO, E AS CÉDULAS!  ' .format(conta))
            print('')
            print ('SEU ATUAL SALDO É:  {}' .format (resultante))

        else:
            print('Seu limite diário é de apenas 2000 reais, para modificar. /n entre em contato conosco em www.bancodaniel.net')

    if opcao == 5 :
        media1 = float(input('Digite o primeiro número: '))
        media2 = float(input('Digite o segundo número: '))
        media = (media1 + media2) / 2
        print("Sua média é {}  " .format(media))
        if media >= 7 :
            print('Aprovado')
        else :
            print('Reprovado')
        
    if opcao == 6 :
        pagamento = int(input('Quanto você recebe?  '))
        if pagamento <= 5000 :
            aumento = pagamento * (20/100) + pagamento
            print("Seu salário Vai subir para: {} Reais " .format(aumento))
        else :
            aumento = pagamento * (10/100) + pagamento
            print('Seu novo salário será de {} Reais ' .format(aumento))

    saida = input("Deseja sair? (S), (N): ")
    if saida == 's' or saida == "S":
        break