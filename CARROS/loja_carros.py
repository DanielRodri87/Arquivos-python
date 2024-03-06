class Carro:
    carros_cadastrados = [] 

    def __init__(self, modelo, ano, cor, preco):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.preco = preco

    def cadastrar_carro(self):
        Carro.carros_cadastrados.append(self)
        print(f"Carro {self.modelo} cadastrado com sucesso!")

    def listar_carros(self):
        if not Carro.carros_cadastrados:
            print("Nenhum carro cadastrado.")
        else:
            print("Carros cadastrados:")
            for carro in Carro.carros_cadastrados:
                print(f"Modelo: {carro.modelo}, Ano: {carro.ano}, Cor: {carro.cor}, Preço: {carro.preco}")

    def atualizar_carro(self, novo_modelo, novo_ano, nova_cor, novo_preco):
        self.modelo = novo_modelo
        self.ano = novo_ano
        
        self.cor = nova_cor
        self.preco = novo_preco
        print(f"Carro atualizado: Modelo - {self.modelo}, Ano - {self.ano}, Cor - {self.cor}, Preço - {self.preco}")

    def deletar_carro(self):
        Carro.carros_cadastrados.remove(self)
        print(f"Carro {self.modelo} deletado com sucesso!")
        
        

while True:
    print("LOJA DANCARRINHO!")
    print("0 - SAIR\n1 - CADASTRAR CARRO\n2 - LISTAR CARROS\n3 - ATUALIZAR CARRO\n4 - DELETAR CARRO")
    opcao = int(input("Digite uma opção: "))

    if opcao == 0:
        break
    elif opcao == 1:
        modelo = input("Digite o modelo do carro: ")
        ano = int(input("Digite o ano do carro: "))
        cor = input("Digite a cor do carro: ")
        preco = float(input("Digite o preço do carro: "))

        novo_carro = Carro(modelo, ano, cor, preco)
        novo_carro.cadastrar_carro()
    elif opcao == 2:
        Carro().listar_carros()
    elif opcao == 3:
        modelo_atualizar = input("Digite o modelo do carro que deseja atualizar: ")
        novo_modelo = input("Digite o novo modelo: ")
        novo_ano = int(input("Digite o novo ano: "))
        nova_cor = input("Digite a nova cor: ")
        novo_preco = float(input("Digite o novo preço: "))

        for carro in Carro.carros_cadastrados:
            if carro.modelo == modelo_atualizar:
                carro.atualizar_carro(novo_modelo, novo_ano, nova_cor, novo_preco)
                break
        else:
            print(f"Carro {modelo_atualizar} não encontrado.")
    elif opcao == 4:
        modelo_deletar = input("Digite o modelo do carro que deseja deletar: ")

        for carro in Carro.carros_cadastrados:
            if carro.modelo == modelo_deletar:
                carro.deletar_carro()
                break
        
        else:
            print(f"Carro {modelo_deletar} não encontrado.")
    else:
        print("Opção inválida. Tente novamente.")
