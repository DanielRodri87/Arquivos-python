palavras =[]
contador = 1
while True:
    if contador <= 5:
        palavra = str(input("Insira uma palavra:"))
        palavras.append(palavra)
        contador+=1
    else:
        break

# printar apenas palavras que começam com a letra 'a'
for i, x in enumerate(palavras):
    if x[0] == 'a':
        print(f'{i} - {x}')
