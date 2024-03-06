
senha = 'admin'
user = 'admin'

while True: 
    print("SEJA BEM-VINDO AO BANCO DANINTER|\n\n")
    
    opcao_menu_1 = int(input("Você já possui uma conta no nosso banco?\n1-Sim\n2-Não\n3-Sair: "))
    
    if opcao_menu_1 == 1:
        opcao_menu_2 = int(input("Deseja fazer Login?\n1-Sim\n2-Nao: "))
        
        if opcao_menu_2 == 1:
            login_user = input("Informe o seu usuário: ")
            login_senha = input("Informe sua senha: ")
            
            if login_senha == senha and login_user == user: 
                print("logado com sucesso")
            else:
                print("Senha ou usuário incorretos")
        else:
            print("Saindo")
    elif opcao_menu_1 == 2:
        print("Informe seus dados: ")
        user = input("Informe o seu usuário: ")
        senha1 = input("Informe sua senha: ")
        senha2 = input("Informe novamente a sua senha: ")
        if senha1 == senha2:
            senha = senha1
        else: 
            print("Informe a senha duas vezes!")
            
    elif opcao_menu_1 == 3:
        print("Saindo")
        break
    
    
