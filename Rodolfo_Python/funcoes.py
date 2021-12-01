# função para retornar o menor número de um vetor
def menor(vetor):
    menor = vetor[0]
    for i in range(1, len(vetor)):
        if vetor[i] < menor:
            menor = vetor[i]
    return menor

vetor = [10, 2, 3, 4, 5, 6, 7, 8, 9, 1]
print(menor(vetor))