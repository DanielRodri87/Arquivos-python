 # Variaveis e tipos
 # Variáveis globais: são variáveis que são acessadas de fora do bloco.
 # Variáveis locais: são variáveis que são acessadas dentro do bloco.
 
valor = 100

def calculo():
    global valor
    valor = 50
    print(valor)

print(calculo())