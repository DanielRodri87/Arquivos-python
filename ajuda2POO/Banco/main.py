#Progama feito pelos alunos: Priscila do E. Santo Sousa e Osmael de Carvalho Gomes

#importanto classe
from conta import Conta
#criando função de buscar conta
def buscaConta(contabancaria):
    nome = (input("DIGITE O  SEU NOME:  "))

    for x in contabancaria:
         if nome == x.nome:
            return x

contabancaria = []


while True:
    print("------------------Opções--------------")
    print("|  1- Cadastrar                      |")
    print("|  2- Alterar conta                  |")
    print("|  3- Buscar conta                   |")
    print("|  4- Fazer um deposito              |")
    print("|  5- Fazer tranferencia             |")
    print("|  6- Fazer saque                    |")
    print("|  7- Excluir conta                  |")
    print("|  8- Listar todos os dados da conta |")
    print("|  9- Sair do progama                |")
    print("--------------------------------------")
    print("")
    opcao = int(input("DIGITE UMA OPÇÃO: "))
    #CADASTRANDO CLIENTE
    if opcao == 1:
       print("Iniciando o cadastro... ")
       cadastro = Conta()
       cadastro.nome = str(input("Digite o seu nome:"))
       cadastro.numero = int(input("Digite o número da conta:"))
       cadastro.senha = int(input("Digite a sua senha:"))
       cadastro.email = str(input("Digite o seu E-mail:"))
       cadastro.agencia = int(input("Digite a Agência:"))
       cadastro.saldo = float(input("Digite o saldo:"))
       
       #Adicionando elementos na lista e concluindo o cadastro
       contabancaria.append(cadastro)
       print("Conta cadastrada!")

    #alterando a conta
    elif opcao == 2:
        print("Alterando a conta..") 
        aux = buscaConta(contabancaria)
        aux.nome = str(input("Digite o seu nome:"))
        aux.numero = int(input("Digite sua nova senha:"))
        aux.email = str(input("Digite o seu novo E-mail:"))
        print("Dados alterados!")

        #None denota falta de valor.
        if aux.nome == None:
            print("Nome não encontrado!")

    elif opcao == 3:
         print("Procurando a conta..")
         aux = buscaConta(contabancaria)
         if aux == None:
            print("Sua conta não existe!")
         else:
            print(aux.nome)
            print(aux.numero)
            print(aux.email)
            print(aux.agencia)
            print(aux.saldo)
    
    #fazer um deposito
    elif opcao == 4:
        print("Fazendo um deposito..")
        aux = buscaConta(contabancaria)

        # A conta não tá nada segura

        if aux == None:
            print("Sua conta não existe!")
        else:
            valor = float(input("Digite o valor do deposito:"))
            aux.depositar(valor)
            print("Deposito realizado com sucesso!")

    #fazer uma tranferencia
    elif opcao == 5:
        pass

    #fazer um saque
    elif opcao == 6:
        print("Fazendo um saque..")
        aux = buscaConta(contabancaria)
        if aux == None:
            print("Sua conta não existe!")
        else:
            valor = float(input("Digite o valor do saque:"))
            aux.sacar(valor)
            print("Saque realizado com sucesso!")

    
    
    #excluindo conta
    elif opcao == 7:
         aux = buscaConta(contabancaria)
         if aux == None:
            print("Sua conta não existe!")
         else:
            contabancaria.remove(aux)
            print("Conta excluida!")


    #listando dados da conta
    elif opcao == 8:
        aux == buscaConta(contabancaria)
        if aux == None:
            print("Sua conta não existe!")
        else:
            print(aux.nome)
            print(aux.numero)
            print(aux.senha)
            print(aux.email)
            print(aux.agencia)
            print(aux.saldo)
    
    
    #se o valor for =0 não existe essa opção então devo demonstrar isso ao úsuario    
    elif opcao == 0:
        print("Essa opção NÃO existe!!!")
    
    #se o valor for maior que 9 não existe opção então devo demonstrar isso ao úsuario
    elif opcao >9:
        print("Essa opção NÃO existe!!!")
    
    #encerrando o progama
    elif opcao ==9:
        print("Encerrando o progama!")
        print("Até a próxima!!!")
        print("Fim do progama!!!")
        break

