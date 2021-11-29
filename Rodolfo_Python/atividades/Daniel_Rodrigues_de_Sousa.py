while True:
    import os

    listadegeladeiras = []
    buscas = []

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

    # Questõeo 1 e 2 --> Fora de funções, porque para funcionar as demais funções necessito de uma lista com dados
    while True:
        capacidade = int(input("Digite a capacidade da geladeira: "))
        marca = input("Digite a marca da geladeira: ")
        cor = input("Digite a cor da geladeira: ")
        g1 = Geladeira(capacidade, marca, cor)
        listadegeladeiras.append(g1)
        print()

        # Questão 2
        continuar = input("Deseja criar outra geladeira? (s/n) ")
        print()
        if continuar == 'n':
            break

    def questao3():       
        # Seja possível buscar por um objeto salvo no arquivos a partir de um dos seus atributos e exibi-lo. Escolha o atributo que desejar para isso.
        busca = input("Digite a marca da geladeira que você quer buscar: ")
        for i in listadegeladeiras:
            if i.marca == busca:
                print(f"A sua geladeira tem {i.capacidade} litros de capacidade, a marca é: {i.marca} e a cor é: {i.cor}")
                break
        else:
            print("Não foi possível encontrar a sua geladeira!")

    def questao4():
        for i in range(len(listadegeladeiras)):
            print(f"A sua geladeira {i+1} tem {listadegeladeiras[i].capacidade} litros de capacidade, a marca é: {listadegeladeiras[i].marca} e a cor é: {listadegeladeiras[i].cor}")
    
    def questao5():
        # alterar elemento da lista
        alterar = input("Digite a marca da geladeira que você deseja modificar: ")
        for i in listadegeladeiras:
            if i.marca == alterar:
                i.marca = input("Digite a nova marca da sua geladeira: ")
                i.capacidade = int(input("Digite a nova capacidade da sua geladeira: "))
                i.cor = input("Digite a nova cor da sua geladeira: ")
                listadegeladeiras.append(i)
                break
            else:
                print("Não foi possível encontrar a sua geladeira! ")       

    os.system('cls')
    
    print('='*70)        
    menu = int(input("Escolha o número para a respectiva questão:\n[3] Questão 3\n[4] Questão 4\n[5] Questão 5\n--> "))
    print('='*70)
    
    if menu == 3:
        questao3()
    elif menu == 4:
        questao4()
    elif menu == 5:
        questao5()
    else:
        print("Opção inválida!")

    saida = input("Deseja sair do programa? (s/n) ").lower()
    if saida == 's':
        break