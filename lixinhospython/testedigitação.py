def maiuscula(palavra):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    alfabeto_maiusculo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    palavra_maiuscula = ''
    for letra in palavra:
        if letra in alfabeto:
            posicao = alfabeto.find(letra)
            palavra_maiuscula += alfabeto_maiusculo[posicao]
        else:
            palavra_maiuscula += letra
    
    return palavra_maiuscula

palavra = input('Digite uma palavra: ')

print(f'Função pronta: {palavra.upper()}')
print(f'Função pronta: {maiuscula(palavra)}')


