class Caneta:
    def __init__(self, cor, marca, escrevendo = False):
        self.cor = cor
        self.marca = marca
        self.escrevendo = escrevendo

    def escrever(self):
        if self.escrevendo == False:
            print(f'A caneta {self.cor}, da marca {self.marca} está escrevendo')
            self.escrevendo = True
        else:
            print('A caneta já está escrevendo')


bic = Caneta('azul', 'bic', True)
bic.escrever()
