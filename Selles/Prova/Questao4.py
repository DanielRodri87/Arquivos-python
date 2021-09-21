size = float(input('Qual é o tamanho do arquivo que você deseja baixar?(Digite em MB) '))
download = float(input('Digite a velocidade da sua internet em Mbps: '))

MBps = download/8
tempo = MBps/size
print(f'{tempo/60} Minutos')