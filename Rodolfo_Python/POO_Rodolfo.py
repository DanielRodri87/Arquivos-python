class Notebook:
    def __init__(self, marca, modelo, tamanho):
        self.marca = marca
        self.modelo = modelo
        self.tamanho = tamanho
        self.ligado = False
        self.__bateria = 100

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def bateria(self):
        return self.__bateria

    def carregar(self, quantidade):
        self.__bateria += quantidade

    def descarregar(self, quantidade):
        self.__bateria -= quantidade