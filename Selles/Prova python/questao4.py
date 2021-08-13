
valorhora = float(input('Quanto você ganha por hora? '))
horasmes = float(input('Quantas horas você trabalha por mês? '))

salariobruto = valorhora * horasmes
inss = (salariobruto/100)*8
sindicato = (salariobruto/100)*5
imposto_de_renda = (salariobruto/100)*11
salarioliquido = salariobruto - sindicato - imposto_de_renda - inss
print()

#saida letra A:
print(f'O seu salário bruto é de {salariobruto} R$')
#saida letra B:
print(f'Desconto INSS é {inss} R$')
#saida letra C:
print(f'Você pagou {sindicato} R$ para o sindicato')
#saida letra D:
print(f'O seu salário líquido é de {salarioliquido} R$')
#saida letra E:
print(f'Salário Bruto: {salariobruto} R$ \n - IR: {imposto_de_renda} R$ \n - INSS: {inss} R$ \n - Sindicato: {sindicato} R$\n = Salário Liquido: {salarioliquido} R$\n')