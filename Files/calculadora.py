class Calculadora:
    def __init__(self):
        self.valor1 = 0
        self.valor2 = 0
        self.resultado = 0
        self.operacao = ''

    def setValor1(self, valor1):
        self.valor1 = valor1

    def setValor2(self, valor2):
        self.valor2 = valor2

    def setOperacao(self, operacao):
        self.operacao = operacao

    def getResultado(self):
        return self.resultado

    def calcular(self):
        if self.operacao == '+':
            self.resultado = self.valor1 + self.valor2
        elif self.operacao == '-':
            self.resultado = self.valor1 - self.valor2
        elif self.operacao == '*':
            self.resultado = self.valor1 * self.valor2
        elif self.operacao == '/':
            self.resultado = self.valor1 / self.valor2
        else:
            print('Operação inválida')


calc = Calculadora()
calc.setValor1(10)
calc.setValor2(5)
calc.setOperacao('+')
calc.calcular()