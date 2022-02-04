bicicletaAlugada = {} 
bicicletas = {} 

class CadastroBike():
    def __init__(self, tipo, chave):
        self._tipo = tipo
        self._chave = chave

    @property  #get tipo
    def tipo(self):
        return self._tipo

    @tipo.setter  #set tipo
    def tipo(self, tipo):
       self._tipo = tipo

    @property  #get id
    def chave(self):
        return self._chave

    @chave.setter  #set id
    def chave(self, chave):
        self._tipo = chave



def inserirBicicleta():
    tipos = ['Volt', 'Volt', 'Nature', 'Nature', 'Urban']
    chave = ['V1', 'V2', 'N1', 'N2', 'U1']
    for i in range(len(tipos)):
        bicicletas[chave[i]] = CadastroBike(tipos[i], chave[i])
inserirBicicleta()

def listarBike(tipo):
    if tipo == "livre":
        for chave, valor in bicicletas.items():
            print(f"Tipo: {valor.tipo}, CHAVE: {chave}")
    else:
        for chave, valor in bicicletaAlugada.items():
            print(f"Tipo: {valor.tipo}, CHAVE: {chave}")

while True:
    print("=================================")
    print("(1) Alugar bicicleta")
    print("(2) Devolver bicicleta")
    print("(3) Listar bicicletas alugadas")
    print("(4) Listar bicicletas disponiveis")
    print("(0) Sair.")
    print("=================================")

    opcao = int(input("Digite a opção escolhida: "))

    if opcao == 1:
        print("=================================")
        listarBike("livre")
        print("=================================")

        chave = input("Digite a CHAVE da bicicleta: ").upper()

        for chave, valor in bicicletas.items():
            if valor.chave == chave:
                bicicletaAlugada[valor.chave] = bicicletas[valor.chave]
                print("Bicicleta alugada com sucesso!")
                del bicicletas[valor.chave]
                break

    elif opcao == 2:
        print("=================================")
        listarBike("ocupada")
        print("=================================")

        chave = input("Digite a CHAVE da bicicleta: ").upper()
        km = int(input("Digite a quilometragem percorrida: "))
        dias = int(input("Digite a quantidade de dias: "))

        for chave, valor in bicicletaAlugada.items():
            if valor.chave == chave:
                bicicletas[valor.chave] = bicicletaAlugada[valor.chave]
                
                if valor.tipo == "Volt":
                    def preco(km, dias):
                        if dias < 15 and km < 1000:
                            return 300
                        elif dias >= 15 and km < 1000:
                            return 300 + (dias - 15) * 5
                        elif dias < 15 and km >= 1000:
                            return 300 + (km - 1000) * 1.5
                        elif dias >= 15 and km >= 1000:
                            return 300 + (km - 1000) * 1.5 + (dias - 15) * 5
                    print(f"O valor a ser pago é R$ {preco(km, dias)}")
                
                elif valor.tipo == "Nature":
                    def preco(km, dias):
                        if dias < 10 and km < 500:
                            return 200
                        elif dias >= 10 and km < 500:
                            return 200 + (dias - 10) * 4
                        elif dias < 10 and km >= 500:
                            return 200 + (km - 500) * 1
                        elif dias >= 10 and km >= 500:
                            return 200 + (km - 500) * 1 + (dias - 10) * 4
                    print(f"O valor a ser pago é R$ {preco(km, dias)}")

                elif valor.tipo == "Urban":
                    def preco(km, dias):
                        if dias < 7 and km < 200:
                            return 100
                        elif dias >= 7 and km < 200:
                            return 100 + (dias - 7) * 3
                        elif dias < 7 and km >= 200:
                            return 100 + (km - 200) * 0.75
                        elif dias >= 7 and km >= 200:
                            return 100 + (km - 200) * 0.75 + (dias - 7) * 3
                    print(f"O valor a ser pago é R$ {preco(km, dias)}")
        
                print("Bicicleta devolvida com sucesso!")
                del bicicletaAlugada[valor.chave]
                break
    
    elif opcao == 3:
        for chave, valor in bicicletaAlugada.items():
            print(f"Tipo: {valor.tipo}, CHAVE: {chave}")

    elif opcao == 4:
        for chave, valor in bicicletas.items():
            print(f"Tipo: {valor.tipo}, CHAVE: {chave}")

    elif opcao == 0:
        break