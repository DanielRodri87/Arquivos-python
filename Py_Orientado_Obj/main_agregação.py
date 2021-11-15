from agregacao import Carrinho_de_compras, Produto

carrinho = Carrinho_de_compras()

p1 = Produto('Camiseta', 45)
p2 = Produto('Xiaomi 9A', 1200)
p3 = Produto('Daniel de plástico', 22000)


carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.listar_produtos()
print(carrinho.soma_total())