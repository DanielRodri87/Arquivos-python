valores = []
maior = 0
indice = 0
for i in range(0, 100):
    valores.append(int(input()))
    if valores[i] > maior:
        maior = valores[i]
        indice = i+1

print(f"{maior}\n{indice}")
    
