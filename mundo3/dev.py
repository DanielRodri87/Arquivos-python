
# def l():
#     print('#'*55)


# l()
# print('oi')
# print('Eu sou o Daniel')
# print('E tenho 16 anos')
# l()

###############################################################################################
# def soma(a,b):
#     s = a+b
#     print(s)


# soma(1,3)
# soma(4,5)

##############################################
def contador(*núm):
    print(núm)
    print(f'O tamanho é: {len(núm)}')


contador(1,2,1,7)
contador(8,7,8,6,5,4,3,6,4,3)
contador(4,0)