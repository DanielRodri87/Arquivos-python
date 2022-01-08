#Joana possui uma sorveteria na cidade de Paulistana-PI, especializada na venda de
#sorvetes e picolés artesanais. A venda dos produtos é tabela por sabor:

# Morango = Sorvete = 12 o kg. Picolé 7 a unidade
# Uva = Sorvete = 9 o kg. Picolé 5 a unidade
# Chocolare = Sorvete = 8,5 o kg. Picolé 3,5 a unidade
# Flocos = Sorvete = 7 o kg. Picolé 4 a unidade

pedidos = []
estoque = []

class Cadastrarencomenda:
    def __init__(self, id, nome, sabor, quantidade, sorvete=0, picole=0):
        self.id = id
        self.nome = nome
        self.sabor = sabor
        self.quantidade = quantidade
        self.sorvete = sorvete
        self.picole = picole

    def pedido(self):
        if self.sabor == 'morango':
            self.sorvete = self.quantidade * 12
            self.picole = self.quantidade * 7
        elif self.sabor == 'uva':
            self.sorvete = self.quantidade * 9
            self.picole = self.quantidade * 5
        elif self.sabor == 'chocolare':
            self.sorvete = self.quantidade * 8.5
            self.picole = self.quantidade * 3.5
        elif self.sabor == 'flocos':
            self.sorvete = self.quantidade * 7
            self.picole = self.quantidade * 4
        else:
            print('Sabor não encontrado')
        pedidos.append([self.id, self.nome, self.sabor, self.quantidade, self.sorvete, self.picole])
        return pedidos

    def apagar_encomenda(self):
        for i in pedidos:
            if i[0] == self.id:
                pedidos.remove(i)
                print('Encomenda removida com sucesso')
                return pedidos
        print('Encomenda não encontrada')
        return pedidos

    def listar_encomenda(self):
        for i in pedidos:
            if i[0] == self.id:
                print(i)
                return i
        print('Encomenda não encontrada')
        return pedidos

# menu
print('')
print('SORVETERIA')
print('1 - Cadastrar encomenda\n2 - Apagar encomenda\n3 - Listar encomenda\n4 - Sair')
print('')
opcao = int(input('Digite a opção desejada: '))
if opcao == 1:
    id = int(input('Digite o ID da encomenda: '))
    nome = input('Digite o nome do cliente: ')
    sabor = input('Digite o sabor do sorvete: ')
    quantidade = int(input('Digite a quantidade: '))
    cadastrarencomenda = Cadastrarencomenda(id, nome, sabor, quantidade)
    cadastrarencomenda.pedido()

elif opcao == 2:
    id = int(input('Digite o ID da encomenda: '))
    cadastrarencomenda = Cadastrarencomenda(id)
    cadastrarencomenda.apagar_encomenda()

elif opcao == 3:
    id = int(input('Digite o ID da encomenda: '))
    cadastrarencomenda = Cadastrarencomenda(id)
    cadastrarencomenda.listar_encomenda()