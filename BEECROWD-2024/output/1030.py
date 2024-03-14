casos = int(input("qtd: "))
count_casos = 0

while count_casos < casos:
    maximo, saltos = map(int, input().split())
    lista = list(range(1, maximo + 1))
    index = 0
    
    while len(lista) > 1:
        index = (index + saltos - 1) % len(lista)
        lista.pop(index)
    
    count_casos += 1
    print(f"Case {count_casos}: {lista[0]}")
