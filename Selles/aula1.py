#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input('Digite um ano'))

if ano % 4 == 0 and ano > 999 and ano < 10000:
    print(f'O ano {ano} é bissexto')

elif ano % 4 != 0 and ano > 999 and ano < 10000:
    print(f'O ano {ano} não é bissexto')
else:
    print('Digite um ano válido')