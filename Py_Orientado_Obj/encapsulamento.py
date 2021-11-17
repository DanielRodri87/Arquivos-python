"""
public, private, protected
_ protected só que pode ser editado, ou seja public com _
__ private impossível sobrescrever
"""

class BaseDeDados:
    def __init__(self):
        self.__dados = {} 

    @property
    def dados(self):
      return self.dados


    def inserir_clientes(self, cpf, nome):
        if 'clientes'not in self.__dados:
            self.__dados['clientes'] = {cpf: nome}
        else:
            self.__dados['clientes'].update({cpf: nome})
    
    def lista_clientes(self):
        for cpf, nome in self.__dados['clientes'].items():
            print(f'{cpf} - {nome}')

    def apaga_clientes(self, cpf):
        del self.__dados['clientes'][cpf]

bd = BaseDeDados()
bd.inserir_clientes(1, 'João')
bd.inserir_clientes(2, 'Maria')
bd.inserir_clientes(3, 'Pedro')

bd.__dados = "Quebrei seu código seu trouxa"

bd.lista_clientes()



