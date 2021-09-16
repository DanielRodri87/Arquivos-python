print('-'*55)
print()
print(' =============+ O M E L H O R J O G O D E FUTEBOL +===========')
print()
print('-'*55)
print()

goleiro = str(input('Escolha o canto para defender: ')).upper()
atacante = str(input('Escolha o canto para chutar: ')).upper()

if goleiro == 'ESQUERDA':
    if goleiro == atacante:
        print(
            ''' -----------------------------------
                |      O                          |
                |     -|-                         |
                |     /\   PEGOU                  |
            '''
        )
    else:
                print(
            ''' -----------------------------------
                |      O                          |
                |     -|-                         |
                |     /\   GOOOL                  |
            '''
        )
        
if goleiro == 'DIREITA':
    if goleiro == atacante:
        print(
            ''' ------------------------------------
                |                             O    |
                |                            -|-   |
                |         PEGOU               /\   |
            '''
        )
    else:
                print(
            ''' ------------------------------------
                |                             O    |
                |                            -|-   |
                |         GOOOL               /\   |
            '''
        )