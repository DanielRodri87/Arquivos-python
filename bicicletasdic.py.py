dic_livres = {}
dic_alugadas = {}

class Bicicletas:
    def __init__(self, locacao, identificador):
        self._locacao = locacao
        self._identificador = identificador

    @property
    def locacao(self):
        return self._locacao
    @locacao.setter
    def locacao(self, locacao):
        self._locacao = locacao

    @property
    def identificador(self):
        return self._identificador
    @identificador.setter
    def identificador(self, identificador):
        self._identificador = identificador

    def alugar(self):
        dic_alugadas[self.identificador] = dic_livres[self.identificador]
        del dic_livres[self.identificador]
        
dic_livres = {"Unidade1":"Volt" ,"Unidade2":"Volt","Unidade3":"Nature","Unidade4":"Nature","Unidade5":"Urban"}
        
while True:
    print("============ MENU ============")
    print("|1| Relação de bikes.")
    print("|2| Alugar bicicletas.")
    print("|3| Desalugar bicicleta.")
    print("|0| Sair.""\n")
    
    opcao = int(input("Digite a opção: "))
    print("\n")
    
    if opcao == 0: 
        break
    
    elif opcao == 1:
        print("====== Relação de bicicletas ======")
        print("Bikes disponíveis para aluguel: ")
        for chave, valor in dic_livres.items():
            print(chave,":", valor)
        print("\n")    
        print("Bikes alugadas: ")
        for chave, valor in dic_alugadas.items():
            print(chave,":",valor)
            
    elif opcao == 2:
        locacao = ['Volt', 'Volt', 'Nature', 'Nature', 'Urban']
        identificador = ['V1', 'V2', 'N1', 'N2', 'U1']

        print("============= Alugar bicicletas =============")
        identificador = str(input("Insira a unidade que deseja alugar: "))
        for chave, valor in dic_livres.items():
            for chave, valor in dic_livres.items():
                if valor.identificador == chave:
                    dic_alugadas[valor.identificador] = dic_livres[valor.identificador]
                    print("Bicicleta alugada com sucesso!")
                    del dic_livres[valor.identificador]
                    break
            
    elif opcao == 3: 
        print("============= Bicicletas alugadas ============")
        for chave, valor in dic_alugadas.items():
            print(chave,":",valor)
        print("")
        identificador = str(input("Insira a unidade que deseja alugar: "))
        if identificador in dic_alugadas.keys():
            #bicicleta = Bicicletas(locacao, identificador)
            dic_livres[identificador] = dic_alugadas[identificador] 
            del dic_alugadas[identificador]
            print(f"A bicicleta {dic_livres[identificador]} foi devolvida!""\n")
            
        else:
            print("Essa bicicleta não foi alugada!""\n")
            
   
