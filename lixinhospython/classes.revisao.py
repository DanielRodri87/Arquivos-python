
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
# O programa deve criar um objeto da classe e mostrar na tela o valor do volume.
class Local:
    def __init__(self, Largura, Comprimento, Altura):
        self.Largura = Largura
        self.Comprimento = Comprimento
        self.Altura = Altura
    def volume(self):
        return self.Largura * self.Comprimento * self.Altura
    

# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.

u1 = Local(6, 7, 5)
print(u1.volume())

# 