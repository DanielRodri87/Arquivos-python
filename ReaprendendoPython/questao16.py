positivos = 0
vetor = []
for i in range(6):
    num = float(input())
    vetor.append(num)
    
for i in range(6):
    if vetor[i] > 0:
        positivos += 1
        
print(f"{positivos} valores positivos")

