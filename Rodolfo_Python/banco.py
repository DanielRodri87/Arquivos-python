from ast import Return


class Conta_Bancaria:
    def __init__(self, agencia, numero, titular, saldo):
        self.agencia = agencia
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, agencia):
        self._agencia = agencia
        