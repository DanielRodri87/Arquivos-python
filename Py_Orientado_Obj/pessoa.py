
class Pessoa:
    ano_atual = 2021
    def __init__(self, nome, idade, comendo=False, falando=False, espancar=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    
    def comer(self, comida):
        if self.comendo:
            print(f'{self.nome} já está bem alimentado')
            return
        if self.falando:
            print(f'{self.nome} não pode comer enquanto está falando')
            return
        print(f'{self.nome} está comendo {comida}')
        self.comendo = True
        
    def parar_de_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False
    
    def falar(self, conversa):
        if self.comendo:
            print(f'{self.nome} não pode falar enquanto está comendo')
            return
        if self.falando:
            print(f'{self.nome} já está falando')
            return
        
        print(f'{self.nome} está falando {conversa}')
        self.falando = True
    
    def calar_a_boca(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return
        print(f'{self.nome} ficará em silencio')
        self.falando = False

    def espancar(self, vitima):
        if self.espancar:
            print(f'{self.nome} já está espancado')
            return
        else:
            print(f'{self.nome} está espancando {vitima}')
        self.espancar = True

    def parar_de_espancar(self):
        if not self.espancar:
            print(f'{self.nome} não está espancando')
            return
        else:
            print(f'{self.nome} parou de espancar')
        self.espancar = False

    def ano_nascimento(self):
        return 2021 - self.idade