#
#       
# ########################### CORES #######################
#
#
#
#
#  VAMOS INDICAR O ESTILO, TEXTO, BACKGROUND RESPECTIVAMENTE
# 
#    TODO CODICO COMEÇA ASSIM \O33[0;0;0m
# 
# 
#       styles: 0 nada, 1 negrito 4 sublinhado 7 inverte os papeis
#       textos: 30 branco, 31 vermelho, 32 verde, 33 amarelo, 34 azul, 35 roxo, 36 ciano, 37 cinza
#       background: 40 branco, 41 vermelho, 42 verde, 43 amarelo, 44 azul, 45 roxo, 46 ciano, 47 cinza
#               
#          EXEMPLO:          print('\033[4;31;41mOlá mundo')
# 
#
#  
# 
nome = 'Daniel'
print('Prazer em te conhecer {}{}{}'.format('\033[4;34m', nome, '\033[m'))