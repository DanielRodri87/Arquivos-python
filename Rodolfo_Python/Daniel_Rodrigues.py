while True:
    menu = int(input("Escolha um número para cada questão:\n[1] Banco\n[2] Calculadora\n[3] Financeamento\n[4] Conta de Energia\n[5] Nome do E-mail\n[6] Provedor do E-mal\n -> "))

    if menu == 1:
        #  Um banco só empresta dinheiro para quem tem o salário maior que R$ 2000 e a idade maior que 18 anos.
        #  Se um jovem de 22 anos ganhando R$ 3500 for pedir empréstimo, o banco aceitará ou não?
        #  Expresse a resposta em um código.

        idade = int(input("Digite a sua idade: "))
        salario = float(input("Digite o seu salário: "))
        if idade >= 18 and salario >= 2000:
            print("O seu empréstimo foi aprovado!")
        else:
            print("O seu empréstimo foi negado!")

    if menu == 2:
        # 2. Leia dois números e que pergunte qual operação o usuário deseja realizar:
        #  soma, subtração, divisão e multiplicação. Exiba o resultado da operação solicitada.
        
        saida = "S"
        while saida == "S":
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação que vai ser utilizada:\n[+] Soma\n[-] Subitração\n[*] Multiplicação\n[/] Divisão\n --> ")
            if operacao == "+":
                print("O resultado da soma é: ", num1 + num2)
            elif operacao == "-":
                print("O resultado da subtração é: ", num1 - num2)
            elif operacao == "*":
                print("O resultado da multiplicação é: ", num1 * num2)
            elif operacao == "/":
                print("O resultado da divisão é: ", num1 / num2)
            else:
                print("Operação inválida!")
            saida = input("Deseja continuar? [S/N]\n--> ").upper()
            
    if menu == 3:
        # Escreva um programa para analisar o financiamento bancário para compra de uma casa. 
        # O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
        #  O valor da prestação mensal não pode ser superior a 30% do salário. 
        # Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar. 
        # De acordo com as informações inseridas, o programa deve dizer se o financiamento será aprovado ou não.
        
        valor_casa = float(input("Digite o valor da casa: "))
        salario = float(input("Digite o seu salário: "))
        anos = int(input("Digite a quantidade de anos para pagar: "))
        prestacao = valor_casa / (anos * 12)
        if prestacao <= salario * 0.3:
            print("O financiamento foi aprovado!")
        else:
            print("O financiamento foi negado!")

    if menu == 4:
        # Escreva um programa que calcule o preço a pagar pela energia elétrica de um imóvel. 
        # Pergunte a quantidade de kwh consumida e o tipo do imóvel: R
        # para residências, I para indústrias e C para comércios. 
        # Calcule o preço a pagar de acordo com as informações a seguir:

        # Residencial - Até 500 kWh (R$ 0,4 por 1 kWH); Acima de 500 kWh (R$ 0,65 por 1 kWH).
        # Comercial - Até 1000 kWh (R$ 0,55 por 1 kWH); Acima de 1000 kWh (R$ 0,6 por 1 kWH).
        # Industrial - Até 5000 kWh (R$ 0,55 por 1 kWH); Acima de 5000 kWh (R$ 0,62 por 1 kWH).

        kwh_usados = float(input("Digite a quantidade de kwh que foi utilizado: "))
        tipo = input("Digite o tipo do imóvel: [R] Residencial, [I] Industrial ou [C] Comercial\n --> ").upper()
        if tipo == "R":
            if kwh_usados <= 500:
                print("O valor a pagar é: R$", kwh_usados * 0.4)
            else:
                print("O valor a pagar é: R$", kwh_usados * 0.65)
        elif tipo == "C":
            if kwh_usados <= 1000:
                print("O valor a pagar é: R$", kwh_usados * 0.55)
            else:
                print("O valor a pagar é: R$", kwh_usados * 0.6)
        elif tipo == "I":
            if kwh_usados <= 5000:
                print("O valor a pagar é: R$", kwh_usados * 0.55)
            else:
                print("O valor a pagar é: R$", kwh_usados * 0.62)
        else:
            print("Tipo de imóvel inválido!")

    if menu == 5:
        #  Crie um programa em que o usuário digite o seu email e o programa informe apenas o seu nome de usuário. 
        # Exemplo:
        # Entrada: rodolfo@gmail.com
        # Saída: rodolfo

        email = input("Digite seu email: ")
        print("Seu nome de usuário é:", email.split("@")[0])

    if menu == 6:
        # Crie um programa em que o usuário digite o seu email e o programa informe o seu provedor de email. 
        # Exemplo:
        # Entrada: rodolfo.paz@hotmail.com
        # Saída: hotmail
        email = input("Digite seu email: ")
        print("Seu provedor de email é:", email.split("@")[1].split(".")[0])