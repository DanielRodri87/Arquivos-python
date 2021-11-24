# como saber o nome de um servido de um email sem split

email = input('Digite seu email: ')
for i in range(len(email)):
    if email[i] == '@':
        if email[i+1] == '.':
            print(f'O servidor é: {email[i+1:len(email)]}')

            


