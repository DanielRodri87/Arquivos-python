dic_livres = {}
dic_alugadas = {}

class Bicicletas():
    def __init__(self, locacao, identificador):
        self._tipo = locacao
        self._chave = identificador

    @property  
    def tipo(self):
        return self._tipo

    @tipo.setter  
    def tipo(self, tipo):
       self._tipo = tipo

    @property  
    def chave(self):
        return self._chave

    @chave.setter  
    def chave(self, chave):
        self._tipo = chave

    def alugar(self):
        dic_alugadas[self.chave] = dic_livres[self.chave]
        del dic_livres[self.chave]

opicao = 2
if opicao == 2:
    print("============= Alugar bicicletas =============")
    identificador = str(input("Insira a unidade que deseja alugar: "))
    for chave, valor in dic_livres.items():
        for chave, valor in dic_livres.items():
            if valor.identificador == chave:
                dic_alugadas[chave] = valor
                print('foi')
                del dic_livres[chave]
            else:
                print('não foi')

print(dic_alugadas)

