
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, porcentagem):
        self.preco = self.preco - (self.preco * porcentagem / 100)

    #Getter Nome
    @property
    def nome(self):
        return self._nome

    #Setter Nome
    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

    # Getter
    @property
    def preco(self):
        return self._preco
    
    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor

p1 = Produto('CELTA', 14000)
p1.desconto(5)
print(p1.nome, p1.preco)
print()

p2 = Produto('FUSCA', 'R$12000')
p2.desconto(5)
print(p2.nome, p2.preco)
print()

p3 = Produto('D10', 25000)
p3.desconto(5)
print(p3.nome, p3.preco)