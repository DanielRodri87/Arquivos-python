#Feita por Daniel

notas = []
print('Digite 4 notas')
for x in range(1, 5):
    notas.append(int(input(f'Digite sua {x}° nota: ')))

m = sum(notas)/4

if m >= 7:
    print(f'Parabéns! você ficou com a média {m} e foi aprovado.')
elif 4 > m:
    print(f'Você ficou com a média {m}, e está reprovado')
elif 4 <= m < 7:
    print(f'Você ficou com a média {m}, e poderá fazer a recuperação') 