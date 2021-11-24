  # Escreva um programa para analisar o financiamento bancário para compra de uma casa. 
        # O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
        #  O valor da prestação mensal não pode ser superior a 30% do salário. 
        # Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar. 
        # De acordo com as informações inseridas, o programa deve dizer se o financiamento será aprovado ou não.


class financiamento:
    def __init__(self):
        self.valor_casa = float(input('Valor da casa: '))
        self.salario = float(input('Salário: '))
        self.anos = int(input('Quantos anos: '))
        self.prestacao = self.valor_casa / (self.anos * 12)
        self.prestacao_maxima = self.salario * 0.3
    def imprime(self):
        if self.prestacao > self.prestacao_maxima:
            print('O financiamento não foi aprovado')
        else:
            print('O financiamento foi aprovado')

imprime = financiamento()
imprime.imprime()
