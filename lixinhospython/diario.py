print('DIÁRIO')
hoje = input('Digite o dia de hoje: ')
lembranças = input('O que aconteceu hoje? ')

arquivo = open("C:\\Users\\Rodrigues\\Desktop\\Arquivos python\\lixinhospython\\diario.txt", 'a')
acontecimentos = list()
acontecimentos.append(f'{hoje}: {lembranças}')
arquivo.writelines(acontecimentos)

