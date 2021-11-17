class TipodeCachoro:
    def __init__(self, nome, raca, comendo=False):
        self.nome = nome
        self.raca = raca
        self.comendo = comendo
    def comer(self):
        print(f'{self.nome} está comendo')
        self.comendo = True
    
    def pararcomer(self):
        if self.comendo:
            print(f'{self.nome} parou de comer')
            self.comendo = False
        else:
            print(f'{self.nome} não está comendo')
            self.comendo = False
    
dog = TipodeCachoro('cachorrão', 'vira-lata')
dog2 = TipodeCachoro('dogão', 'pincher')
print(dog.raca, dog2.raca)
