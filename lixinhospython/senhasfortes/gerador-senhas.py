import random

min = "abcdefghijklmnopqrstuvwxyz"
mai = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
sinais = "!@#$%&*()"
juncao = min + mai + num + sinais

tamanho = int(input("Qual o tamanho da sua senha? "))
local = str(input('Essa senha será para qual site/aplicativo? '))
senha = "".join(random.sample(juncao,tamanho))

print(f"Sua senha de {tamanho} digitos foi criada: {senha}")

arquivo = open("C:\\Users\\Rodrigues\\Desktop\\Arquivos python\\lixinhospython\\senhasfortes\\Senhas.txt", "a")
frases = list()
frases.append(f"{local}: {senha} \n")

arquivo.writelines(frases)

