def questao():
    print("Questão 1")
    print("1. Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.")
    numero = int(input("Digite um número inteiro: "))
    contador = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            contador += 1
    if contador == 2:
        print("O número digitado é primo.")
    else:
        print("O número digitado não é primo.")
    print("")