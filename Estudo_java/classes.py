class Maiusculo:
    def __init__(self, texto):
        self.texto = texto

    def trocar_maiusculo(self):
        for i in range(len(self.texto)):
            if self.texto[i].isupper():
                self.texto = self.texto[:i] + self.texto[i].lower() + self.texto[i+1:]

            else:
                self.texto = self.texto[:i] + self.texto[i].upper() + self.texto[i+1:]

    def __str__(self):
        return self.texto


texto = input('Digite um texto: ')
maiusculo = Maiusculo(texto)
maiusculo.trocar_maiusculo()
print(maiusculo)