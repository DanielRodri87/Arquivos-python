agenda = {}
qtd = int(input('Você deseja registrar quantos CPFs? '))

for x in range(qtd):
    print(f'{x+1}° Pessoa')
    cpf = int(input('Digite o seu CPF: '))
    nome = str(input('Digite o seu nome: '))
    idade = int(input('Digite sua idade: '))
    cell = int(input('Digite o seu número de telefone: '))
    agenda[cpf] = nome, idade, cell

for keys, values in agenda.items():  
    print(f'CPF: {keys} Dados: {values}')
    
