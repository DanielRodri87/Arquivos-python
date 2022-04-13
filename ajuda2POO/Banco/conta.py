class Conta:
    def __init__(self, nome, numero, senha, email, agencia, saldo):
            self.nome = nome
            self.numero = numero 
            self.senha = senha
            self.email = email
            self.agencia = agencia
            self.saldo = saldo

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print('Saque realizado com sucesso!')
        else:
            print('Saldo insuficiente!')

    def depositar(self, valor):
        self.saldo += valor
        print('Deposito realizado com sucesso!')

    def transferir(self, valor, conta):
        pass

    def extrato(self):
        print('Extrato:')
        print('Nome: {}'.format(self.nome))
        print('Número: {}'.format(self.numero))
        print('Saldo: {}'.format(self.saldo))



    