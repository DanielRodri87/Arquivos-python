while True:
    import os
    menu = int(input("Escolha o número para a respectiva questão:\n[1] Questão 1\n[2] Questão 2\n[3] Questão 3\n[4] Questão 4\n[5] Questão 5\n--> "))
    os.system('cls')

    listadegeladeiras = []

    class Geladeira:
            def __init__(self, capacidade, marca, cor, aberta=False):
                self.capacidade = capacidade
                self.marca = marca
                self.cor = cor
                self.alimentos = []
                self.aberta = aberta
            
            def abrir(self):
                if self.aberta == True:
                    print("A geladeira já está aberta!")
                else:
                    self.aberta = True
                    print("Abrindo a geladeira... ")
            
            def fechar(self):
                if self.aberta == False:
                    print("A geladeira já está fechada!")
                else:
                    self.aberta = False
                    print("Fechando a geladeira... ")
            
            def guardar(self, alimento):
                if self.aberta:
                    if self.capacidade > len(self.alimentos) + 1:
                        self.alimentos.append(alimento)
                        print("Guardando alimento na geladeira... ")
                    else:
                        print("Não foi possível adicionar, a geladeira está cheia!")
                else:
                    print("A geladeira está fechada!")
                
            def retirar(self, alimento):
                if self.aberta:
                    if alimento in self.alimentos:
                        self.alimentos.remove(alimento)
                        print("Retirando alimento da geladeira... ")
                    else:
                        print("Não foi possível retirar, o alimento não está na geladeira!")
                else:
                    print("A geladeira está fechada!")

    if menu == 1:
        capacidade = int(input("Digite a capacidade da geladeira: "))
        marca = input("Digite a marca da geladeira: ")
        cor = input("Digite a cor da geladeira: ")
        g1 = Geladeira(capacidade, marca, cor)
        print(f"A sua geladeira tem {g1.capacidade} litros de capacidade, a marca é: {g1.marca} e a cor é: {g1.cor}")

    elif menu == 2:

        while True:
            capacidade = int(input("Digite a capacidade da geladeira: "))
            marca = input("Digite a marca da geladeira: ")
            cor = input("Digite a cor da geladeira: ")
            g1 = Geladeira(capacidade, marca, cor)
            listadegeladeiras.append(g1)
            continuar = input("Deseja cadastrar outra geladeira? [s/n]: ").lower()
            print()
            if continuar == 'n':
                break
      
        escolha = input('Você deseja buscar uma geladeira? [s/n]: ').lower()

        if escolha == 's':
            os.system('cls')
            busca = input("Digite a marca da geladeira que você quer buscar: ")
        for i in range(len(listadegeladeiras)):
            if busca == listadegeladeiras[i].marca:
                print('='*70)
                print('Geladeira encontrada!\n')
                print(f"Capacidade: {listadegeladeiras[i].capacidade} litros:\nMarca: {listadegeladeiras[i].marca}\nCor: {listadegeladeiras[i].cor}")
        else:
            break

    saida = input("\nDeseja sair? [s/n] ").lower()
    if saida == 's':
        break

            