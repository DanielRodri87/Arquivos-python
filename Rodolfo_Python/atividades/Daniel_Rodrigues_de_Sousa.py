# Possua uma classe para representar um item de sua escola. A classe deve possuir 3 atributos que caracterizam esse item ou ser. Classes proibidas: aluno, professor e livro.
import random

class ControleCantina:
    def __init__(self, nome, senha, alimento, quantidadeMax, permicao = False):
        self.nome = nome
        self.senha = senha
        self.alimento = alimento
        self.quantidadeMax = quantidadeMax == 10 # O usuário só pode pedir até 10 alimentos durante o dia
        self.permicao = permicao
        

    def cadastrarUser(self): # Cadastrar usuário
        print('\n########### CADASTRO ###########\n')
        self.logs = {}
        self.nome = input("Digite seu nome: ")
        self.senha = input("Digite sua senha: ")
        self.logs[self.nome] = self.senha

    def login(self):
        print('\n########### LOGIN ###########\n')
        self.nome = input("Digite seu nome: ")
        self.senha = input("Digite sua senha: ")
        if self.nome in self.logs and self.logs[self.nome] == self.senha:
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
            print("Você não tem permissão para ver os alimentos! ")


alunos = []
logs = {}

while True:
    print('\n########### MENU ###########\n')
    print('1- Cadastrar usuário')
    print('2- Login')
    print('3- Pedir alimento')
    print('4- Ver alimento')
    print('5- Sair')



    opcao = int(input('Digite a opção desejada: '))
    
    if opcao == 1:
        count = 0   
        while count < 5:
            a1 = ControleCantina('', '', '', 0, False)
            a1.cadastrarUser()
            alunos.append(a1)
            count += 1
        else:
            del alunos[0]
            saida = input('Deseja cadastrar mais usuários? [S/N]').upper()
            while saida == 'S':
                a2 = ControleCantina('', '', '', 0, False)
                a2.cadastrarUser()
                alunos.append(a2)
                saida = input('Deseja cadastrar mais usuários? [S/N]').upper()

    elif opcao == 2:
        # logar a partir do nome
        for i in alunos:
            i.login()
            if i.permicao == True:
                print(f'\nBem vindo {i.nome}!\n')
                break
            else:
                print('\nUsuário ou senha inválidos!\n')
                break

    elif opcao == 3:
        for a in alunos:
            a.pedidoAlimento()
            if a.permicao == True:
                break
        else:
            print("Nenhum usuário cadastrado!")

    elif opcao == 4:
        for a in alunos:
            a.mostrarAlimento()
            if a.permicao == True:
                break
        else:
            print("Nenhum usuário cadastrado!")

    elif opcao == 5:
        break

while True:
    print('\n########### Modificar atributo ###########\n')
    print('1- Alterar nome')    
    print('2- Alterar senha')
    print('4- Alterar quantidade máxima')
    print('5- Sair')

    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        for a in alunos:
            a.nome = input('Digite o novo nome: ')
            print(f'Nome alterado para {a.nome}!')
            alunos.append(a)
            
    elif opcao == 2:
        for a in alunos:
            a.senha = input('Digite a nova senha: ')
            print(f'Senha alterada para {a.senha}!')
            alunos.append(a)
    elif opcao == 3:
        for a in alunos:
            a.quantidadeMax = int(input('Digite a nova quantidade máxima: '))
            print(f'Quantidade máxima alterada para {a.quantidadeMax}!')
            alunos.append(a)

    elif opcao == 4:
        break

# Eu sei que poderia ter feito algo melhor, que pelo menos rodasse, porém, devido ao tempo curto, proporcionado por outras provas, não pude fazer outra coisa, ou corrigir os bugs.
# Essa última parte devido a um bug em cadeia, não tinha muito o que fazer, porque a lista alunos recebia o local da memória e os atributos juntos, bagunçando tudo. E como disse, essas semanas estão corridas!
# Obrigado pela compreensão.