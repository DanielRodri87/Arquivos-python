# Possua uma classe para representar um item de sua escola. A classe deve possuir 3 atributos que caracterizam esse item ou ser. Classes proibidas: aluno, professor e livro.
import random



class controleCantina:
    def __init__(self, user, senha, alimento, quantidadeMax, permicao = False):
        self.user = user
        self.senha = senha
        self.alimento = alimento
        self.quantidadeMax = quantidadeMax == 10 # O usuário só pode pedir até 10 alimentos durante o dia
        self.permicao = permicao
        

    def cadastrarUser(self): # Cadastrar usuário
        print('\n########### CADASTRO ###########\n')
        self.logs = {}
        self.user = input("Digite seu nome: ")
        self.senha = input("Digite sua senha: ")
        self.logs[self.user] = self.senha

    def login(self):
        print('\n########### LOGIN ###########\n')
        self.user = input("Digite seu nome: ")
        self.senha = input("Digite sua senha: ")
        if self.user in self.logs and self.logs[self.user] == self.senha:
            print("Login realizado com sucesso!")
            self.permicao = True
        else:
            print("Usuário ou senha inválidos!")
            self.permicao = False

    def pedidoAlimento(self):
        if self.permicao == True:
            lanche = ['maçã', 'banana', 'pão', 'pizza', 'suco', 'refrigerante', 'água', 'café', 'chá', 'leite']
            self.alimento = random.choice(lanche)
            self.quantidadeMax = int(input(f"O lanche de hoje é {self.alimento} e você pode pedir até 10 unidades. Digite quantas unidades você deseja: "))
            if self.quantidadeMax <= 10:
                print("Pedido realizado com sucesso!")
            else:
                print("Quantidade máxima de alimentos excedida!")

        else:
            print("Você não tem permissão para realizar pedidos!")


    def mostrarAlimento(self):
        if self.permicao == True:
            print(f"O lanche de hoje é {self.alimento} e você pode pediu {self.quantidadeMax} unidades.")
        else:
            print("Você não tem permissão para ver os alimentos!")
 
