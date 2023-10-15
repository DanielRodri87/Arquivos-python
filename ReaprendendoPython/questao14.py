a, b, c, d = map(float, input().split())
media = (a+b+c+d)/4


print(f"Media: {media:.1f}")
if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input("Nota do Exame: "))
    if (media+exame)/2 > 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media Final: ",(media+exame)/2)
