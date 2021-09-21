nota1=float(input("Digite nota 1: "))
nota2=float(input("Digite nota 2: "))

media = (nota1 + nota2) / 2

if media >=9 and media <= 10:
   conceito = "A"
elif media >= 7.5 and media <=9:
   conceito = "B"
elif media >= 6 and media <=7.5:
    conceito = "C"
elif media >= 4 <=6:
    conceito = "D"
elif media > 0 and media <=4:             
    conceito = "E"
else: 
    print("Houve um problema, tente novamente.")


if conceito == "A" or conceito == "B" or conceito == "C":
    resultado = "Aprovado!"
else: 
    resultado = "Reprovado"
print()
print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print()
print(f"Conceito: {conceito}")
print(f"Resultado: {resultado}")