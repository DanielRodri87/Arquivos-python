# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
'''lista = []

for c in range(5):
    lista.append(int(input('Numero: ')))
print(lista)'''


letrasListas = []
consoantes = 0
vogais = 0

for repeticao in range(10):
    letrasListas.append(str(input("Digite 10 letras: ")))
    letras = letrasListas[repeticao]

    if(letras not in ('a','e','i','o','u')):
        consoantes += 1
    

print(f"Essa foi a lista que você digitou: {letrasListas}")
print(f"Tem no total: {consoantes} consoantes. ")
