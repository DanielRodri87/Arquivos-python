# dicionario = {}
# print(dicionario.values()) Retorna valores, tipo o nome do filme
# print(dicionario.keys()) mostra o que é cada, filme, ano e tudo
# print(dicionario.items()) mostra tudo

ola = {}
for x in range(5):
    nome = input('Seu nome: ')
    idade = int(input('Quantos anos vc tem? '))
    ola[nome] = [idade]
for nome, idade in ola.items():
    print(f'{nome}: idade: {idade}')
print(ola.keys())