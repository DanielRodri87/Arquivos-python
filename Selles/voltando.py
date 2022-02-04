notas = []
qtd = 0
for alunos in range(1,11):
    print(f'Aluno {alunos}')
    for repticao in range(4):
        notas.append(float(input("Digite suas 4 notas: ")))
todos = [notas[0:4], notas[4:8], notas[8:12], notas[12:16], notas[16:20], notas[20:24], notas[24:28], notas[28:32], notas[32:36], notas[36:40]]
for x in todos:
    media = sum(x) / 4
    if media >= 7:
        qtd += 1
print(f'A quantidade de alunos com média maior ou igual a 7.0 é: {qtd}')