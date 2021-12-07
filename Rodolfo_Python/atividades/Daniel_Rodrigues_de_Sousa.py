import random

class ControleCantina:
    def __init__(self, nome, senha, alimento, quantidadeMax):
        self.nome = nome
        self.senha = senha
        self.alimento = alimento
        self.quantidadeMax = quantidadeMax == 10 # O usuário só pode pedir até 10 alimentos durante o dia

alunos = []

# Criando os 3 alunos iniciais
matriculado1 = ControleCantina('Daniel', '123', 'Pão', 10)
matriculado2 = ControleCantina('Rodolfo', '321', 'Refrigerante', 10)
matriculado3 = ControleCantina('Rafael', '456', 'Suco', 10)

# Adicionando os alunos criados a lista
alunos.append(matriculado1)
alunos.append(matriculado2)
alunos.append(matriculado3)


while True: # Inicio do menu de escolhas
    print('\n########### MENU ###########\n')
    print('1 - Cadastrar 5 usuários ')
    print('2 - Alterar atributo')
    print('3 - Sair')

    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1: # Opção 1 = Criando uma lista de usuários
        count = 3   # Contador já começa com 3 pois já tem 3 alunos cadastrados
        while count < 5: # Enquanto o contador for menor que 5, ou seja, enquanto não tiver 5 alunos cadastrados
            nome = input('Digite o nome do usuário: ')
            senha = input('Digite a senha do usuário: ')
            print('\n###############################\n')
            alimento = random.choice(['Pizza', 'Batata Frita', 'Refrigerante', 'Suco', 'Biscoito', ''])
            quantidadeMax = 10
            a1 = ControleCantina(nome, senha, '', quantidadeMax) # Criando um objeto do tipo ControleCantina
            
            alunos.append(a1) # Adicionando o objeto a lista de alunos
            count += 1
        else: # Se não for menor que 5, então o contador é igual a 5, ou seja, já tem 5 alunos cadastrados.	
            saida = input('Deseja cadastrar mais usuários? [S/N]').upper() # O usuário pode cadastrar mais usuários
            while saida == 'S':
                del alunos[0] # Deletando o primeiro usuário cadastrado
                nome = input('Digite o nome do usuário: ')
                senha = input('Digite a senha do usuário: ')
                alimento = random.choice(['Pizza', 'Batata Frita', 'Refrigerante', 'Suco', 'Biscoito', 'Feijoada'])
                quantidadeMax = 10
                a2 = ControleCantina(nome, senha, '', quantidadeMax)
                
                alunos.append(a2)
                count += 1
    elif opcao == 2: # Caso a opção seja 2, o usuário pode alterar os atributos de um aluno
        print('\n########### ALTERAR ATRIBUTO ###########\n')   #
        print('1 - Alterar nome')                               #
        print('2 - Alterar senha')                              # --> Novo menu de escolhas, mas dessa vez é para modifcar os atributos
        print('3 - Alterar quantidade máxima')                  #
        print('4 - Voltar ao menu')                             #
        opcao = int(input('Digite a opção desejada: '))

        if opcao == 1: # Alterando o nome do aluno
            nome = input('Digite o nome do usuário: ') # O usuário digita o nome do aluno que deseja alterar
            for i in alunos: # Percorrendo a lista de alunos
                if i.nome == nome: # Se o nome do aluno for igual ao nome digitado pelo usuário
                    i.nome = input('Digite o novo nome: ')  # O usuário digita o novo nome
                    print('Alterado com sucesso!')
            else:
                print('Usuário não encontrado') # Se o nome digitado não for igual ao nome de algum aluno, o usuário é avisado

        elif opcao == 2: # As ações se repetem, só que agora para a senha
            nome = input('Digite o nome do usuário: ')
            for i in alunos:
                if i.nome == nome:
                    i.senha = input('Digite a nova senha: ')
                    print('Alterado com sucesso!')
            else: 
                print('Usuário não encontrado')
                    
        elif opcao == 3: # As ações se repetem, só que agora para a quantidade máxima
            nome = input('Digite o nome do usuário: ')
            for i in alunos:
                if i.nome == nome:
                    i.quantidadeMax = int(input('Digite a nova quantidade máxima: '))
                    print('Alterado com sucesso!')
            else:
                print('Usuário não encontrado')

    elif opcao == 3: # Saida do programa
        break

    fim = input('Deseja sair? [S/N]').upper() # Saida final do programa
    if fim == 'S':
        break
  