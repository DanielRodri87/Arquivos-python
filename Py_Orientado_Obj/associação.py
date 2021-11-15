class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None
    
    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

    
class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    def escrever(self):
        print(f'A caneta {self.__marca} está escrevendo')

    @property
    def marca(self):
        return self.__marca

class Marquina_de_escrever:
    def __init__(self):
        pass

    def escrever(self):
        print(f'A maquina está escrevendo...')
