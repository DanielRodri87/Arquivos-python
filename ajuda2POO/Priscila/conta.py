class Conta():
    def _init_(self, nome, numero, senha, email, agencia, saldo, deposito, saque, transferencia):
            self.nome = nome
            self.numero = numero 
            self.senha = senha
            self.email = email
            self.agencia = agencia
            self.saldo = saldo
            self.deposito = deposito
            self.saque = saque
            self.tranferencia = transferencia 


    
    
    def imprimirSaldo(self):
        print("O saldo da conta é ",self.saldo)




