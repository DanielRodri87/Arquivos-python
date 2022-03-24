from pessoa import Pessoa

lista_Pessoas = []

while True:
    print('[1] Cadastrar Pessoa\n[2] Listar Pessoas\n[3] Sair\n--> ', end='')
    opcao = int(input())
    if opcao == 1:
        print('Digite o nome: ', end='')
        nome = input()
        print('Digite o CPF: ', end='')
        cpf = input()
        lista_Pessoas.append(Pessoa(nome, cpf))

    elif opcao == 2:
        for pessoa in lista_Pessoas:
            print(pessoa)

    elif opcao == 3:
        break