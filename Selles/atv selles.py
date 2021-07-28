import os
print('')
print(70*'-')
print('')
print('==================DANIEL CALCULOS==================')
print('')
print(70*'-')

print('''
        [1] SOMA
        [2] SUBTRAÇÃO
        [3] MULTIPLICAÇÃO
        [4] DIVISÃO
        [5] MÉDIA
    ''')

menu = int(input('Escolha a operação para o cálculo: '))

if menu == 1:
    os.system('cls') 
    s1 = int(input('Digite o primeiro valor: '))
    s2 = int(input('Digite o segundo número: '))
    soma1 = s1+s2
    print('O resultado é: {} '.format(soma1))
    print(type(soma1))

elif menu == 2:
    os.system('cls') 
    m1 = int(input('Digite o primeiro valor: '))
    m2 = int(input('Digite o segundo número: '))
    sub = m1-m2
    print('O resultado é: {} '.format(sub))
    print(type(sub))
elif menu == 3:
    os.system('cls')
    mul1 = int(input('Digite o primeiro valor: '))
    mul2 = int(input('Digite o segundo número: '))
    mult = mul1*mul2
    print('O resultado é: {} '.format(mult)) 
    print(type(mult))
elif menu == 4:
    os.system('cls') 
    d1 = int(input('Digite o primeiro valor: '))
    d2 = int(input('Digite o segundo número: '))
    div = d1/d2
    print('O resultado é: {} '.format(div))
    print(type(div))

elif menu == 5:
    os.system('cls') 
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo número: '))
    sm = (n1+n2)/2
    print('Sua média é {}'.format(sm))
    if sm >= 7:
        print('Parabéns! Você foi aprovado ')
    else:
        print('Infelizmente você foi reprovado!')   
    print(type(sm))