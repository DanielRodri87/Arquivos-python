print('''
    SOMA        ---->    [01]
    SUBTRAÇÃO   ---->    [02]
    DIVISÃO     ---->    [03]
    DIVISÃO INTEIRA ---> [04]
    MULTIPLICAÇÃO ---->  [05]
''')
print("Segue acima as opções disponíveis, e agradecemos por utilizar nosso app")
print('')

menu = float(input("ESCOLHA QUAL OPERAÇÃO VOCÊ DESEJA UTILIZAR: "))

if menu == 1:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o primeiro número: "))
    s = n1 + n2
    print(s)
if menu == 2:
    s1 = float(input("Digite o primeiro número: "))
    s2 = float(input("Digite o primeiro número: "))
    sub = s1 - s2
    print(sub)
if menu == 3:
    d1 = float(input("Digite o primeiro número: "))
    d2 = float(input("Digite o primeiro número: "))
    div = d1 / d2
    print(div)   
if menu == 4 :
    d1i = float(input("Digite o primeiro número: "))
    d2i = float(input("Digite o primeiro número: "))
    divi = d1i // d2i
    print(divi)  
if menu == 5 :
    mult1 = float(input("Digite o primeiro número: "))
    mult2 = float(input("Digite o primeiro número: "))
    mult = mult1 // mult2
    print(mult) 
