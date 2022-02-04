dic_livres = {"Unidade1":"Volt" ,"Unidade2":"Volt","Unidade3":"Nature","Unidade4":"Nature","Uniddae5":"Urban"}
dic_alugadas = {}

class Bicicletas:
    def __init__(self, locacao, identificador):
        self.locacao = locacao
        self.identificador = identificador

    @property
    def locacao(self):
        return self._locacao
    @locacao.setter
    def locacao(self, locacao):
        self._locacao = locacao

    @property
    def identificador(self):
        return self._identificador
    @locacao.setter
    def identificador(self, identificador):
        self.identificador = identificador

    
while True:
    print("============MENU============")
    print("|1| Relação de bikes.")
    print("|2| Alugar bicicletas.")
    print("|3| Desalugar bicicleta.")
    print("|0| Sair.")

    opcao = int(input("Digite a opção: "))

    if opcao == 0: 
        break
    
    elif opcao == 1:
        print("====== Relação de bicicletas ======")
        print("\n")
        print("Bikes disponíveis para aluguel: ")
        for chave, valor in dic_livres.items():
            print(chave,":", valor)
        print("\n")    
        print("Bikes alugadas: ")
        for chave, valor in dic_alugadas.items():
            print(chave,":",valor)
            
    elif opcao == 2:
        print("=============Alugar BIKES=============")
        identificador = str(input("Insira a unidade que deseja alugar: "))
        if identificador in dic_livres.keys():
            #bicicleta = Bicicletas(locacao, identificador) - Karielly, essa parte é muito importante e deu errado.
            #nome_do_dicionário[chave] = valor (new value ad)
            dic_alugadas[identificador] = dic_livres[identificador] 
            del dic_livres[identificador]
            print(f"A bicicleta{dic_alugadas[identificador]} alugada!")
        else:
            print("Essa bicicleta já foi alugada!")
            
    elif opcao == 3: 
        for bicicleta in dic_alugadas:
            print(
                f"Tipo: {bicicleta.locacao}, Quilometragem: {bicicleta.quilometragem}, identificador: {bicicleta.identificador}"
                )
        bike = input("Digite o identificador da bicicleta que deseja desalugar: ")
        for bicicleta in dic_alugadas:
            if bike == bicicleta.identificador:
                dias = int(input("Insira a quantidade de dias que \na bike ficou alugada: "))
                km_rodados = int(input("Insira a quilometragem rodada: "))
                if bicicleta.identificador == "Volt01" or bicicleta.identificador == "Volt02":
                    if km_rodados > 1000:
                        multa_km = (km_rodados - 1000) * 1.5
                    elif dias > 15:
                        multa_dias = (dias - 15) * 5
                    valor_total = multa_km + multa_dias + 300
                elif bicicleta.identificador == "Nature01" or bicicleta.identificador == "Nature02":
                    if km_rodados > 500:
                        multa_km = (km_rodados - 500) * 1
                    elif dias > 10:
                        multa_dias = (dias - 10) * 5
                    valor_total = multa_km + multa_dias + 200
                elif bicicleta.identificador == "Urban01":
                    if km_rodados > 200:
                        multa_km = (km_rodados - 200) * 0.75
                    elif dias > 7:
                        multa_dias = (dias - 7) * 0.75
                    valor_total = multa_km + multa_dias + 100

                print(f"Bicicleta {bike} desalugada com sucesso!")
                print("==============================")
                print(f"Valor total: {valor_total}")
                dic_livres.append(bicicleta)
                dic_livres.remove(bicicleta)
                break
            else:
                print("Bicicleta não encontrada!")
                break