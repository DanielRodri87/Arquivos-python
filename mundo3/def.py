
# def contador(inicio, fim, pulo):
#     count = inicio
#     while count <= fim:
#         print(f'{count}', end="-")
#         count += pulo

# contador(1, 10, 2)

def criar_lista(tam):
    lista = []
    for i in range(tam):
        lista.append(i+1)
    return lista

tam = int(input('Digite o tamanho da lista: '))
print(criar_lista(tam))
