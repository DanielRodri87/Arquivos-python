#Progama feito pelos alunos: Priscila do E. Santo Sousa e Osmael de Carvalho Gomes

#importanto classe
from conta import Conta

import os
#criando função de cadastrar conta.
def cadastrarconta(contabancaria):
        cadastro = Conta()
        print ("Iniciando cadastro...")
        print("****************************")
        cadastro.nome = str(input("Digite o seu nome:"))
        cadastro.numero = int(input("Digite o número da conta:"))
        cadastro.senha = int(input("Digite a sua senha:"))
        cadastro.email = str(input("Digite o seu E-mail:"))
        cadastro.agencia = int(input("Digite a Agência:"))
        cadastro.saldo = 1000
        print("******************************")
        
        #Adicionando elementos na lista e concluindo o cadastro
        contabancaria.append(cadastro)
        print("Conta cadastrada!")
        print("*******************************")
        

#criando função de buscar conta
def buscaConta(contabancaria):
    numero = int(input("DIGITE O NUMERO DA SUA CONTA:  "))
    print("*************************************")

    for x in contabancaria:
        if numero == x.numero:
            return x
    

#função para tranferencia
def tansferencia(contabancaria):
    print("Iniciando a transferência...")
    print("****************************************")
    conta_pricipal = int(input("Digite o número da conta principal: "))
    conta_secundaria = int(input("Digite o número da conta secundária: "))
    valor = int(input("Digite o valor da transferência:"))


    for x in contabancaria:
        if conta_pricipal == x.numero:
            conta_pricipal = contabancaria.index(x)
            break

    for x in contabancaria:
        if conta_secundaria == x.numero:
            conta_secundaria = contabancaria.index(x)
            break

    if contabancaria[conta_pricipal].saldo < valor:
        print("Saldo insuficiente!")
        print("**************************")
        return
    else:
        # Se o saldo permitir, transferir
        contabancaria[conta_pricipal].saldo -= valor
        contabancaria[conta_secundaria].saldo += valor
        print("Transferência realizada com sucesso!")
        print("****************************************")

#lista para guardar os dados
contabancaria = []

while True:
    os.system("cls")
    print("********Opções*********")
    print("|  1- Cadastrar       |")
    print("|  2- Alterar conta   |")
    print("|  3- Excluir conta   |")
    print("|  4- Listar contas   |")
    print("|  5- Acessar conta   |")
    print("|  6- Sair do progama |")
    print("***********************")
    print("")
    opcao = int(input("DIGITE UMA OPÇÃO: "))
    #CADASTRANDO CLIENTE
    if opcao == 1:
        cadastrarconta(contabancaria)
 
 #ALTERANDO CONTA
    elif opcao == 2:
        print("Iniciando a alteração da conta...")
        alterar = buscaConta(contabancaria)
        if alterar == None:
            print("ESSA CONTA NÃO EXISTE!!!")
        else:
            alterar.nome = str(input("Digite o seu nome:"))
            alterar.numero = int(input("Digite o número da conta:"))
            alterar.senha = int(input("Digite a sua senha:"))
            alterar.email = str(input("Digite o seu E-mail:"))
            alterar.agencia = int(input("Digite a Agência:"))
            alterar.saldo = 1000
            print("CONTA ALTERADA!")

#  ACESSANDO CONTA
    elif opcao == 5:
        
        print("Acessando conta!")
        numBusca = int(input("Numero para busca> "))
        for c in contabancaria:
            if c.numero == numBusca:
                while True:
                    os.system("pause")
                    os.system("cls")
                    print("*****OPÇÕES*****")
                    print("|1 - Saldo      |")
                    print("|2 - Sacar      |")
                    print("|3 - Depositar  |")
                    print("|4 - Transferir |")
                    print("|5 - Sair       |" )
                    print("*****************")
                    op = int(input("digite a opção que desejas:  "))
                    
                    #imprimindo o saldo
                    if op == 1:
                        c.imprimirSaldo()

                    #SAQUE
                    elif op ==2:
                        print("Iniciando o saque...")
                        saque = buscaConta(contabancaria)
                        if saque == None:
                            print("ESSA CONTA NÃO EXISTE!!!")
                        else:
                            saque.saldo = saque.saldo - float(input("Digite o valor do saque:"))
                            print("Saque realizado!")
                    #DEPOSITO
                    elif op == 3:
                        print("Iniciando o depósito...")
                        depositar = buscaConta(contabancaria)
                        if depositar == None:
                            print("ESSA CONTA NÃO EXISTE!!!")
                        else:
                            depositar.saldo = depositar.saldo + float(input("Digite o valor do depósito:"))
                            print("Depósito realizado!")
                    #TRANSFERENCIA
                    elif op ==4:
                         tansferencia(contabancaria)
                    #ENCERRANDO
                    elif op ==5:
                        print("Encerrando...")
                        break
#EXCLUINDO
    elif opcao ==3:
        print("Iniciando a exclusão da conta...")
        excluir = buscaConta(contabancaria)
        if excluir == None:
            print("ESSA CONTA NÃO EXISTE!!!")
        else:
            contabancaria.remove(excluir)
            print("Conta excluida!")

#LISTANDO CONTAS
    elif opcao ==4:
            print("Listando contas...")
            for n in contabancaria:
                print("***************************************")
                print(f"Nome:{n.nome} | E-mail:{n.email}")
            
 
  #encerrando
    elif opcao ==6:
        print("Encerrando...")
        print("Encerrado!")
        break
    os.system("pause")