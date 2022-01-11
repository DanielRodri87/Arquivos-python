class Caneta:
    def __init__(self, cor, ponta, carga):
        self.cor = cor
        self.ponta = ponta
        self.carga = carga
        self.tampada = False

    def escrever(self, texto):
        if self.tampada:
            print("A caneta está tampada!")
        else:
            print(f"Estou escrevendo uma caneta {self.cor} com ponta {self.ponta}")
            self.carga -= len(texto)

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False