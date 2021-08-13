################################# QUESTÃO 1 ####################################
'''lista = []
print("Digite 5 números:")
for c in range(5):
    lista.append(int(input('Numero: ')))
print(lista)'''
###############################

'''letrasListas = []
consoantes = 0


for repeticao in range(10):
    letrasListas.append(str(input("Digite 10 letras: ")))
    letras = letrasListas[repeticao]

    if(letras not in ('a','e','i','o','u')):
        consoantes += 1
    

print(f"Essa foi a lista que você digitou: {letrasListas}")
print(f"Tem no total: {consoantes} consoantes. ")'''

###########################################################################3

'''lista = []

print('Digite 10 números reais: ')
for c in range(10):
    lista.append(float(input("Digite: ")))

lista.reverse()
print(f'Essa é a ondem inversa do que você digitou: {lista}')
lista.sort()
print(f'A ordem crescente é: {lista}')
lista.sort(reverse = True)
print(f'A ordem descrescente é: {lista}')'''


################################################## QUESTÃO 6 #########################################
'''notas = []
qtd = 0
for alunos in range(1,11):
    print(f'Aluno {alunos}')
    for repticao in range(4):
        notas.append(float(input("Digite suas 4 notas: ")))

#Descobrindo a quantidade de aprovados
if sum(notas[:4])/4 >= 7:
    qtd += 1
if sum(notas[3:8])/4 >= 7:
    qtd += 1
if sum(notas[7:12])/4 >= 7:
    qtd += 1
if sum(notas[11:16])/4 >= 7:
    qtd += 1
if sum(notas[15:20])/4 >= 7:
    qtd += 1
if sum(notas[19:24])/4 >= 7:
    qtd += 1
if sum(notas[23:28])/4 >= 7:
    qtd += 1
if sum(notas[27:32])/4 >= 7:
    qtd += 1
if sum(notas[31:36])/4 >= 7:
    qtd += 1
if sum(notas[35:])/4 >= 7:
    qtd += 1
#saida
print(f'{qtd} Alunos acima da média')'''
#############################QUESTÃO 7######################################333
'''Import numpy
numeros = []
print('Digite 5 números')

for c in range(1, 6):
    numeros.append(int(input(f'Número {c}: ')))
soma = sum(numeros)
mult = numpy.prod(numeros)

print(f'Lista de números digitados: {numeros}\n Essa é a soma de todos os números: {soma}\nEssa é a multiplicação de todos os números: {mult}')
'''
###########################################QUESTÃO 9################################################################

'''a = []
print('Digite 10 números')
for c in range(1, 11):
    a.append(int(input(f'Número {c} ')))
soma_quadrados = a[0]**2 + a[1]**2 + a[2]**2 + a[3]**2 + a[4]**2 + a[5]**2 + a[6]**2 + a[7]**2 + a[8]**2 + a[9]**2 
print(f'A soma dos quadrados é: {soma_quadrados}')'''

##################################### QUESTÃO 8 #####################################################################

'''idade = []
peso = []

for c in range(1, 6):
    print(f'pessoa {c} ')
    idade.append(int(input('Digite sua idade: ')))
    peso.append(float(input('Digite seu peso: ')))
peso.reverse()
idade.reverse()

print(f'A lista de idades ao contrário é: {idade}')
print(f'A lista de peso ao contrário é: {peso}')'''

################################################# QUESTÃO 10 OUTRO PC ############################

'''vetor1 = []
vetor2 = []
for c in range(1,11):
    vetor1.append(int(input(f'Digite 10 números para o vetor1, esse é o número {c}: ')))
for c2 in range(1,11):
    vetor2.append(int(input(f'Digite 10 números para o vetor2, esse é o número {c2}: ')))

vetor3 = [*sum(zip(vetor1,vetor2),())]
print(vetor3)'''

################################  13  #####################################33

'''vetor1 = []
vetor2 = []
vetor3 = []

for c in range(1,11):
    vetor1.append(int(input(f'Digite 10 números para o vetor1, esse é o número {c}: ')))
for c2 in range(1,11):
    vetor2.append(int(input(f'Digite 10 números para o vetor2, esse é o número {c2}: ')))
for c3 in range(1,11):
    vetor3.append(int(input(f'Digite 10 números para o vetor2, esse é o número {c3}: ')))

vetor4 = [*sum(zip(vetor1,vetor2,vetor3),())]
print(vetor4)'''


############################    12    ##########################################

idades = [32,89,65,34,22,34,76,12,13,29,28,54,24,32,89,65,34,22,34,76,12,13,29,28,54,24,12,10,34,2]
alturas = [1.87,1.65,1.23,1.89,1.90,1.32,1.56,1.87,1.04,1.21,1.06,1.76,1.58,1.87,1.65,1.23,1.89,1.90,1.32,1.56,1.87,1.04,1.21,1.06,1.76,1.58,1.00,2.34,1.72,1.67]
media = sum(alturas)/30
qtd = 0

for c in range(1, len(idades)):
    if idades[c] >= 13:
        if alturas[c] < media:
            qtd += 1
print(qtd)



