class Cadastro:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    @property
    def nome(self):
        return self._nome

    #Setter Nome
    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()
    
    @property
    def cpf(self):
        return self._cpf
    
    #Setter CPF
    @cpf.setter
    def cpf(self, valor):
        if not isinstance(valor, str):
            valor = str(valor)
            self._cpf = valor.replace('.', '').replace('-', '')
        else:
            self._cpf = valor.replace('.', '').replace('-', '')
        valor = self._cpf
