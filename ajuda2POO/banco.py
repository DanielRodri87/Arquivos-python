
class Banco:
    def __init__(self):
        self.contas = {}

    def adicionar(self, conta):
        self.contas[conta.nome] = conta

    def remover(self, nome):
        if nome in self.contas:
            del self.contas[nome]
        else:
            print("Conta nao encontrada")

    def alterar(self, nome):
        if nome in self.contas:
            conta = self.contas[nome]
            while True:
                print(" 1 alterar nome")
                print(" 2 alterar email")
                print(" 3 alterar numero")
                print(" 4 voltar")

                opcao = int(input("escolha a opcao: "))
                if opcao == 1:
                    conta.nome = input("Digite o seu nome: ")
                elif opcao == 2:
                    conta.email = input("Digite seu email: ")
                elif opcao == 3:
                    conta.numero = int(input("Digite um numero "))
                elif opcao == 4:
                    break
                else:
                    print("opcao invalida")
        else:
            print("Conta nao encontrada")

    def buscar(self, nome):
        if nome in self.contas:
            conta = self.contas[nome]
            print(f"Nome: {conta.nome}")
            print(f"Email: {conta.email}")
            print(f"Numero: {conta.numero}")
        else:
            print("Conta nao encontrada")

    def listar(self):
        for nome, conta in self.contas.items():
            print(f"Nome: {conta.nome}")
            print(f"Email: {conta.email}")
            print(f"Numero: {conta.numero}")

class Conta:
    def __init__(self):
        self.nome = ""
        self.agencia = ""
        self.saldo = 0
        self.numero = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def transferir(self, valor, conta):
        if self.saldo >= valor:
            self.saldo -= valor
            conta.saldo += valor
        else:
            print("Saldo insuficiente")

    def extrato(self):
        print(f"Saldo: {self.saldo}")



def main():
    banco = Banco()
    while True:
        print(" 1 adicionar contato")
        print(" 2 remover contato")
        print(" 3 alterar contato")
        print(" 4 buscar contato")
        print(" 5 listar contatos")
        print(" 6 sair")
        opcao = int(input("escolha a opcao: "))
        if opcao == 1:
            conta = Conta()
            conta.nome = input("Digite o seu nome: ")
            conta.email = input("Digite seu email: ")
            conta.numero = int(input("Digite um numero "))
            banco.adicionar(conta)
        elif opcao == 2:
            nomepararemocao = input("Digite o nome do contato que voce quer remover: ")
            banco.remover(nomepararemocao)
        elif opcao == 3:
            nomeparaalterar = input("Qual contato voce quer alterar: ")
            banco.alterar(nomeparaalterar)
        elif opcao == 4:
            nomeparabuscar = input("Digite o nome do contato que voce quer buscar: ")
            banco.buscar(nomeparabuscar)
        elif opcao == 5:
            banco.listar()
        elif opcao == 6:
            break
        else:
            print("opcao invalida")

if __name__ == "__main__":
    main()
