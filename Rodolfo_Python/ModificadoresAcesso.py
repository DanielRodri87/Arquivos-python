# getter e setters
import os
class Cliente():
    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, valor):
        self._nome = valor.title() 
    @property
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self, valor):
        self._cpf = valor
        
    def cadastrar(self):
        cliente[self.cpf] = self.nome
        return cliente

    def pesquisarCliente():
        cpf = input('Digite o CPF: ')
        if cpf in cliente:
            print(cliente[cpf])
        else:
            print('CPF não encontrado')
    
cliente = {}
    

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
