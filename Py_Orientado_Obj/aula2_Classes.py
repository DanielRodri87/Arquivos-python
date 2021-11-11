class Pessoa2:
    ano_atual = 2021
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

# p1 = Pessoa2.por_ano_nascimento("Daniel", 2005)
p1 = Pessoa2("Daniel", 16)
print(p1.idade)
p1.get_ano_nascimento()