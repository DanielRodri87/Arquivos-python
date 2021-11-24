# class BancoBradesco:
#     saldo = 0
#     agencia = ''
#     conta = ''
#     def depositar(self, valor):
#         self.saldo += valor

#     def sacar(self, valor):
#         self.saldo -= valor

#     def printar_saldo(self):
#         print(self.saldo)

#     def transferir(self, valor, conta_destino):
#         self.sacar(valor)
#         conta_destino.depositar(valor)

# contadaniel = BancoBradesco()
# contarodolfo = BancoBradesco()

# contadaniel.depositar(30000)
# contadaniel.transferir(100, contarodolfo)
# contadaniel.printar_saldo()
# contarodolfo.printar_saldo()

class Conta:
    def __init__(self, nome, agencia, conta, saldo):
        self.nome = nome
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor
    
    def transferir(self, valor, conta_destino):
        self.sacar(valor)
        conta_destino.depositar(valor)

    def printar_saldo(self):
        print(self.saldo)



banco = []
while True:
    print('1 - Criar conta')
    print('2 - Depositar')
    print('3 - Sacar')
    print('4 - Saldo')
    print('5 - sair')
    
    opcao = int(input('Digite uma opção: '))
    if opcao == 1:
        nome = input('Digite o nome: ')
        agencia = input('Digite a agencia: ')
        conta = input('Digite a conta: ')
        saldo = float(input('Digite o saldo: '))
        conta_nova = Conta(nome, agencia, conta, saldo)
        banco.append(conta_nova)
        print(f'Cona do titular {nome} criada com sucesso! ')
    elif opcao == 3:
        conta_busca = input('Digite a conta: ')
        for conta in banco:
            if conta.conta == conta_busca:
                valor = float(input('Digite o valor: '))
                conta.sacar(valor)
                print('Saque realizado com sucesso!')
                break
        else:
            print('Conta não encontrada!')
    if opcao == 6:
        # consulta de conta
        conta_busca = input('Digite a conta: ')
        for conta in banco:
            if conta.conta == conta_busca:
                conta.printar_saldo()
                break
        else:
            print('Conta não encontrada!')
    if opcao == 5:
        break