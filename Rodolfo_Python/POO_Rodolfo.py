class TimesFutebol:
    def __init__(self, nome, jogadores, tecnico):
        self.nome = nome
        self.jogadores = jogadores
        self.tecnico = tecnico

flamengo = TimesFutebol('Flamengo', 'Gabigol; Daniel; Filipe Luis; Jean', 'Ronaldo')

jogadores = []
jogadores.append(flamengo.jogadores)

for x in jogadores:
    print(x)
