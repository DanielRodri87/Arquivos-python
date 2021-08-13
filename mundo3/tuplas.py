#tuplas são imutáveis
#contagem começa do 0, 0, 1, 2, 3


'''lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche[2:])            PARA IR ATÉ O FINAL'''
##########################################################
'''lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}') 
print('Fim')   ------>  FOR AÍ '''

#############################################################

'''lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
for cont in range(0, len(lanche)):
    print(lanche[cont]) ------> lenddo em relação a poição'''

############################################################

'''lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(sorted(lanche)) -> Para deixar em ordem'''

#####################################################33
'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(2)) #-> criando uma nova tupla
'''
##################################################3
'''pessoa = ('Daniel', 16, 'Masculino', 71.4)
print(pessoa)
del(pessoa)'''
##########################EXERCICIOS###########################

numeros = ('Zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove','dez', 'onze', 'doze', 'treze', 'catorze','quinze', 'dezesseis', 'dezessete', 'dezoito','dezenove', 'vinte')

while True:
    interacao_usuario = int(input('Digite um número entre 0 e 20: '))
    if 0 <= interacao_usuario and interacao_usuario <= 20:
        break
print(f'O número que você digitou por extenso é: {numeros[interacao_usuario]}')

