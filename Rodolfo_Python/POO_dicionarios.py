# Crie um programa para cadastrar clientes utilizando o CPF como chave e o seu nome como valor.
#  Caso o CPF não esteja contido no dicionário, o usuário deve digitar o nome. Caso o CPF já exista
# , o programa deve informar o nome do cliente. O programa só encerrará caso o usuário digite “0”.

import os

cliente = {}

class Cliente():
    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def cadastrar(self):
        cliente[self.cpf] = self.nome
        return cliente
    
    def pesquisarCliente():
        cpf = input('Digite o CPF: ')
        if cpf in cliente:
            print(cliente[cpf])
        else:
            print('CPF não encontrado')
    

while True:
    try:
        opc = int(input('Digite:\n[0] Para sair\n[1] para cadastrar um cliente\n[2] Pesquisar\n-> '))
        if opc == 1:
            os.system('cls')
            print('-----------------------')
            cpf = input('Digite o CPF: ')
            nome = input('Digite o nome: ')
            print('-----------------------')
            if cpf in cliente:
                print(f'\nO cliente {cliente[cpf]} já está cadastrado.\n')
            else:
                print(f'\nO cliente {nome} foi cadastrado com sucesso.\n')
                cliente = Cliente(cpf, nome).cadastrar()
                print(cliente)
        elif opc == 2:
            os.system('cls')
            Cliente.pesquisarCliente()
        elif opc == 0:
            break

    except ValueError:
        print('\nDigite apenas números!\n')
        
    
    