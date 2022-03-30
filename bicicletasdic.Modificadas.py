class Contato:
    def __init__(self, nome, email, numero):
        self.nome = nome
        self.email = email
        self.numero = numero

    def _str_(self):
        return f'Nome: {self.nome}, Email: {self.email}, Numero: {self.numero}'


def main():
    agenda = {}
    while True:
        print('1 - Novo contato')
        print('2 - Alterar contato')
        print('3 - Remover contato')
        print('4 - Buscar contato')
        print('5 - Sair')
        opcao = int(input('Digite a opção desejada: '))

        if opcao == 1:
            chave = int(input('Digite a chave: '))
            nome = input('Digite o nome: ')
            email = input('Digite o email: ')
            numero = input('Digite o numero: ')
            agenda[chave] = Contato(nome, email, numero)
        
        # Alterar contato
        elif opcao == 2:
            chave = int(input('Digite a chave: '))
            if chave in agenda: # -> Se a chave existir, edite-a
                nome = input('Digite o nome: ')
                email = input('Digite o email: ')
                numero = input('Digite o numero: ')
                agenda[chave] = Contato(nome, email, numero) # -> Atualiza o contato

            else:
                print('Chave não encontrada')

        # Remover contato
        elif opcao == 3:
            chave = int(input('Digite a chave: '))
            if chave in agenda:
                del agenda[chave]
            else:
                print('Chave não encontrada')

        # Buscar contato
        elif opcao == 4:
            chave = int(input('Digite a chave: '))
            if chave in agenda:
                # informações
                print(f'Nome: {agenda[chave].nome}, Email: {agenda[chave].email}, Numero: {agenda[chave].numero}')
            else:
                print('Chave não encontrada')

        # Sair
        elif opcao == 5:
            break
    
if __name__ == '__main__':
    main()