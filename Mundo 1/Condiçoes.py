numero = 3
print('Vamos jogar? \n Escola um número de 0 à 5')
print('pensando...')
print('Huuum, número escolhido, tente acertar')
advinhe = int(input('Tente acertar'))                                              <----- DESAFIO 01 OK
if advinhe == 3:
   print('Acertou!')
else:
   print('O número era: {}, e infelizmente você errou'.format(numero))


velocidade = int(input('Qual a velocida em que o veiculo ultrapassou? '))
if velocidade > 80:
   multa = (velocidade - 80)*7                                                                               <--- DESAFIO 02 OK
   print('VOCÊ EXCEDEU O LIMITE DE VELOCIDADE, TOTAL A PAGAR É: {}'.format(multa))



numero=int(input('Dê um número qualquer:  '))
if numero//2 == numero/2:
   print('O número {} é par!'.format(numero))                                                  <----- Desafio 03 ok
else:
   print('O número {} é ímpar!'.format(numero))


viagem = int(input('QUANTOS KM VOCê PERCORREU EM SUA VIAGEM: '))
if viagem <= 200:
   preco = viagem*0.5
   print('Sua viagem custou {} Reais'.format(preco))                              <---- DESAFIO 04 OK
else:
   preco = viagem*0.45
   print(preco)


















