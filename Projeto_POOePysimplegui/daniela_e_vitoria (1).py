# Listas que vao ser usadas
sorveteria_estoque = []

lista_ultimas_vendas = []

# Preços Sorvetes -----
s_morango = 12 #Kg
s_uva = 9 #Kg
s_chocolate = 8.5 #Kg
s_flocos = 7 #Kg

# Preços Picoles -------
p_morango = 7 #unidade
p_uva  = 5 #unidade
p_chocolate = 3.5 #unidade
p_flocos = 4 #unidade

class Estoque:
    def __init__(self, sorvete, picole, quantidade):
        self.sorvete = sorvete
        self.picole = picole
        self.quantidade = quantidade

    def mostrar_estoque():
        print("\nEstoque atual:")
        for i in range(len(sorveteria_estoque)):
            print(sorveteria_estoque[i].sorvete, sorveteria_estoque[i].picole, sorveteria_estoque[i].quantidade)

class Historico_Vendas:
    def __init__(self, nome, sorvete, picole, quantidade):
        self.nome = nome
        self.sorvete = sorvete
        self.picole = picole
        self.quantidade = quantidade

while True:
    print("Seja bem vindo ao sistema de sorveteria")
    menu = int(input('1 - Listar estoque\n2 - Realizar venda\n3 - Adicionar estoque\n4 - Remover estoque\n5 - Consultar lucro\n6 - Histórico de vendas\n7 - Sair\n'))

    if menu == 1:
        Estoque.mostrar_estoque()
    if menu == 2:
        print("\nRealizar Venda\n")
        tipo = int(input('1 - Sorvete\n2 - Picole\n'))
        if tipo == 1:
            tipo = 'Sorvete'
            sabor = int(input('1 - Morango\n2 - Uva\n3 - Chocolate\n4 - Flocos\n'))
            quantidade = int(input('Quantidade: '))
            if sabor == 1:
                sabor = 'Morango'
            elif sabor == 2:
                sabor = 'Uva'
            elif sabor == 3:
                sabor = 'Chocolate'
            elif sabor == 4:
                sabor = 'Flocos'

            lista_ultimas_vendas.append(Historico_Vendas(tipo, sabor, quantidade))
            print('Venda realizada!')

        elif tipo == 2:
            tipo = 'Picole'
            p_sabor = int(input('1 - Morango\n2 - Uva\n3 - Chocolate\n4 - Flocos\n'))
            quantidade = int(input('Quantidade: '))
            if p_sabor == 1:
                p_sabor = 'Morango'
                preco = quantidade * p_morango
            elif p_sabor == 2:
                p_sabor = 'Uva'
                preco = quantidade * p_uva
            elif p_sabor == 3:
                p_sabor = 'Chocolate'
                preco = quantidade * p_chocolate
            elif p_sabor == 4:
                p_sabor = 'Flocos'
                preco = quantidade * p_flocos

            lista_ultimas_vendas.append(Historico_Vendas(tipo, sabor, quantidade))
            print('Venda realizada!')

    if menu == 3:
        print("\nAdicionar Estoque\n")
        tipo = int(input('1 - Sorvete\n2 - Picole\n'))
        if tipo == 1:
            tipo = 'Sorvete'
            sabor = int(input('1 - Morango\n2 - Uva\n3 - Chocolate\n4 - Flocos\n'))
            quantidade = int(input('Quantidade: '))
            if sabor == 1:
                sabor = 'Morango'
            elif sabor == 2:
                sabor = 'Uva'
            elif sabor == 3:
                sabor = 'Chocolate'
            elif sabor == 4:
                sabor = 'Flocos'
            # adicionar na lista estoque
            sorveteria_estoque.append(Estoque(tipo, sabor, quantidade))
            print('Estoque atualizado!')

        elif tipo == 2:
            tipo = 'Picole'
            p_sabor = int(input('1 - Morango\n2 - Uva\n3 - Chocolate\n4 - Flocos\n'))
            quantidade = int(input('Quantidade: '))
            if p_sabor == 1:
                p_sabor = 'Morango'
            elif p_sabor == 2:
                p_sabor = 'Uva'
            elif p_sabor == 3:
                p_sabor = 'Chocolate'
            elif p_sabor == 4:
                p_sabor = 'Flocos'

            sorveteria_estoque.append(Estoque(tipo, sabor, quantidade))


    elif menu == 4:
        print("\nRemover Estoque\n")
        tipo = int(input('1 - Sorvete\n2 - Picole\n'))
        if tipo == 1:
            tipo = 'Sorvete'
            sabor = int(input('1 - Morango\n2 - Uva\n3 - Chocolate\n4 - Flocos\n'))
            quantidade = int(input('Quantidade: '))
            if sabor == 1:
                sabor = 'Morango'
            elif sabor == 2:
                sabor = 'Uva'
            elif sabor == 3:
                sabor = 'Chocolate'
            elif sabor == 4:
                sabor = 'Flocos'

            for i in range(len(sorveteria_estoque)):
                if sorveteria_estoque[i].sorvete == tipo:
                    if sorveteria_estoque[i].quantidade > quantidade:
                        sorveteria_estoque[i].quantidade -= quantidade
                        print('Estoque atualizado!')
                    else:
                        print('Quantidade insuficiente!')
                        break
        if tipo == 2:
            tipo = 'Picole'
            p_sabor = int(input('1 - Morango\n2 - Uva\n3 - Chocolate\n4 - Flocos\n'))
            quantidade = int(input('Quantidade: '))
            if p_sabor == 1:
                p_sabor = 'Morango'
            elif p_sabor == 2:
                p_sabor = 'Uva'
            elif p_sabor == 3:
                p_sabor = 'Chocolate'
            elif p_sabor == 4:
                p_sabor = 'Flocos'

            for i in range(len(sorveteria_estoque)):
                if sorveteria_estoque[i].picole == tipo:
                    if sorveteria_estoque[i].quantidade > quantidade:
                        sorveteria_estoque[i].quantidade -= quantidade
                        print('Estoque atualizado!')
                    else:
                        print('Quantidade insuficiente!')
                        break
            
    elif menu == 5:
        print("\nConsultar Saldo\n")
        print('Saldo: R$', sum(sorveteria_estoque.preco))         
    elif menu == 6:
        pass
    elif menu == 7:
        print("\nSaindo do sistema...")
        break