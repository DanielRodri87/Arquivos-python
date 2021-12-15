class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

while True:
    print('Canil')

    print('1 - Cadastrar\n2- Apagar cachorro')

    opcao = int(input('Digite a opção: '))
    cachorros = []
    if opcao == 1:
        nome = input('Digite o nome do cachorro: ')
        raca = input('Digite a raça do cachorro: ')
        idade = int(input('Digite a idade do cachorro: '))
        cachorro = Cachorro(nome, raca, idade)
        # adiconar na lista os atributos
        cachorros.append(cachorro)

    elif opcao == 2:
        nome = input('Digite o nome do cachorro: ')
        for cachorro in cachorros:
            if cachorro.nome == nome:
                cachorros.remove(cachorro)
                print('Cachorro removido')
                break
        else:
            print('Cachorro não encontrado')