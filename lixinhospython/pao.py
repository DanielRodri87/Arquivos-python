print('digite um número de 1 a 4 de acordo com a opção abaixo')
print('1 = soma\n2 = subtração\n')
nume = int(input('Escolha a opção: '))
if nume == 1 :
    valor1 = int(input("digite o primeiro valor : "))
    valor2 = int(input("digite o segundo valor : "))
    soma = valor1 + valor2
    print('A soma entre {} e {}  resulta em {}'.format(valor1,valor2,soma))
    print(type(soma))
elif nume == 2: 
    sub1 = int(input("digite o primeiro valor : "))
    sub2 = int(input("digite o segundo valor : ")) 
    subtracao = sub1-sub2
    print('A subtração entre {} e {}  resulta em {}'.format(sub1,sub2,subtracao))
    print(type(subtracao))