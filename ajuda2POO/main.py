from contato import Contato
dict_contatos = {}
while True:
#elcimara e georgia

    print(" 1 adicionar contato")
    print(" 2 remover contato")
    print(" 3 alterar contato")
    print(" 4 buscar contato")
    print(" 5 listar contatos")
    print(" 6 sair")
    opcao = int(input("escolha a opcao: "))
    if opcao == 1:
        contatos = Contato() 
        contatos.nome = input("Digite o seu nome: ")
        contatos.email = input("Digite seu email: ")
        contatos.numero = int(input("Digite um numero "))
        dict_contatos[contatos.nome] = contatos

    elif opcao == 2:
        nomepararemocao = input("Digite o nome do contato que voce quer remover: ")

        if nomepararemocao in dict_contatos:
            del dict_contatos[nomepararemocao]
        else:
            print("Contato nao encontrado")
        
    elif opcao == 3:
        nomeparaalterar = input("Qual contato voce quer alterar: ")
        if nomeparaalterar in dict_contatos:
            while True:
                print(" 1 alterar nome")
                print(" 2 alterar email")
                print(" 3 alterar numero")
                print(" 4 voltar")
                
                opcao = int(input("escolha a opcao: "))
                if opcao == 1:
                    dict_contatos[nomeparaalterar].nome = input("Digite o seu nome: ")
                elif opcao == 2:
                    dict_contatos[nomeparaalterar].email = input("Digite seu email: ")
                elif opcao == 3:
                    dict_contatos[nomeparaalterar].numero = int(input("Digite um numero "))
                elif opcao == 4:
                    break
                else:
                    print("opcao invalida")
        else:
            print("Contato nao encontrado")
    
    elif opcao == 4:

        nomeparabuscar = input("Digite o nome do contato que voce quer buscar: ")
        if nomeparabuscar in dict_contatos:
            contatos = dict_contatos[nomeparabuscar]
            print(f"Nome: {contatos.nome}")
            print(f"Email: {contatos.email}")
            print(f"Numero: {contatos.numero}")
        else:
            print("Contato nao encontrado")

    elif opcao == 5:
        for nome, contatos in dict_contatos.items():
            print(f"Nome: {contatos.nome}")
            print(f"Email: {contatos.email}")
            print(f"Numero: {contatos.numero}")
            print("-"*20)

    elif opcao == 6:
        print("saindo...")
        break

    
   



