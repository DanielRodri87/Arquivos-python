import os
lista_televisoes = []
log_marcas = []

class InputError(Exception):
    def __init__(self, value):
        self.value = value
    
    def input_num(self):
        while True:
            try:
                num = int(input(self.value))
                return num
            except ValueError:
                print("Valor inválido, digite novamente.")
                os.system("pause")
                os.system("cls")
                menu()
                continue

class Televisao:
    def __init__(self, marca, canal, volume):
        self.marca = marca
        self.canal = canal
        self.volume = volume
        
    def volume_tv(self, volume):
        self.volume = volume
        return self.volume 
    
    def canal_tv(self, canal):
        self.canal = canal
        return self.canal

def buca_marca(marca_tv):
    for televisor in lista_televisoes:
        if televisor.marca == marca_tv:
            return lista_televisoes.index(televisor)

def alterar_televisao(televisao):
    os.system("cls")
    print(f'1 - Marca: {televisao.marca}')
    print(f'2 - Canal: {televisao.canal}')
    print(f'3 - Volume: {televisao.volume}')
    print('-'*30)
    print('0 - Sair')
    print('-'*30)
    opcao = InputError("Digite a opção desejada: ").input_num()

    if opcao == 1:
        marca = input('Digite a marca: ')
        televisao.marca = marca
    elif opcao == 2:
        canal = InputError('Digite o canal: ').input_num()
        televisao.canal_tv(canal)
    elif opcao == 3:
        volume = InputError('Digite o volume: ').input_num()
        televisao.volume_tv(volume)
    elif opcao == 0:
        return 0
    else:
        return False

def menu():
    os.system("cls")
    print("Digite (1) para criar uma TV.")
    print("Digite (2) para alterar seus atributos.")
    print("Digite (3) para listar todas as TVs.")
    print("Digite (0) para sair.")

def inserir_televisao():
        print("="*46)

        marca = input("Digite a marca da TV: ")
        canal = InputError("Digite o canal da TV: ").input_num()
        volume = InputError("Digite o volume da TV: ").input_num()

        if marca not in log_marcas and marca != '':
            televisor = Televisao(marca, canal, volume)
            lista_televisoes.append(televisor)

            print("="*46)
            print(f"TV {len(lista_televisoes)} criada com sucesso!")
            print("="*46)
            log_marcas.append(marca)
            os.system("pause")

        else:
            print("="*46)
            print("TV já cadastrada ou marca inválida.")
            print("="*46)
            os.system("pause")
            return False

def get_quantidade_televisores(): 
    quantidade_televisoes = len(lista_televisoes)
    if quantidade_televisoes == 0:
        print("="*46)
        print("Não existem TVs cadastradas.")
        print("="*46)
        os.system("pause")
        return False

def retornar_televisor_por_marca(marca_tv):
    try:
        televisao = lista_televisoes[buca_marca(marca_tv)]
    except TypeError:
        print("TV não encontrada.")
        os.system("pause")
        return False
    return televisao

def retornar_televisor_por_num(num_tv):
    try:
        televisao = lista_televisoes[num_tv-1]
    except IndexError:
        print("TV não encontrada.")
        os.system("pause")
        return False
    return televisao

def main():
    while True:
        menu()

        opcao = InputError("Digite a opção desejada: ").input_num()

        if opcao == 1:
            if inserir_televisao() == False:
                continue
        
        elif opcao == 2: # Alterar atributos da TV
            while True:
                os.system("cls")

                if get_quantidade_televisores() == False:
                    break
                else:
                    print("Opções de busca: \n(1) Nome marca\n(2) Número da TV\n(0) Para sair")
                    busca = InputError("Digite a opção desejada: ").input_num()

                    if busca == 1:
                        os.system("cls")

                        marca_tv = input("Digite a marca da TV: ")
                        
                        televisao = retornar_televisor_por_marca(marca_tv)
                        if televisao == False:
                            continue
                        if alterar_televisao(televisao) == False:
                            continue
                        elif alterar_televisao(televisao) == 0:
                            break
                    
                    elif busca == 2:
                        os.system("cls")
                        num_tv = InputError("Digite o número da TV: ").input_num()

                        televisao = retornar_televisor_por_num(num_tv)
                        if televisao == False:
                            continue
                        alterar_televisao(televisao)

                    elif busca == 0:
                        break
                    
                    else:
                        continue

        if opcao == 3:
            os.system("cls")
            if len(lista_televisoes) == 0:
                print("Não existem TVs cadastradas.")
            for i, tv in enumerate(lista_televisoes):
                print(f'{i+1} - {f"Marca: {tv.marca}, canal: {tv.canal}, volume: {tv.volume}"}') 
            print()
            os.system("pause")

        if opcao == 0:
            break
main()