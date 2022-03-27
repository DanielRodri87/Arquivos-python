from pessoa import Pessoa


class MyApp:
    def __init__(self):
        self.list_person = []

        MyApp.__run(self)

    def add_person(self, person):
        self.list_person.append(person)
    
    def find_person(self, person):
        for p in self.list_person:
            if p.CPF == person.CPF:
                return p
        return None
    
    def __run(self):
        while True:
            print('1 - Adicionar Pessoa')
            print('2 - Buscar Pessoa')
            print('3 - Sair')
            print('\n')
            option = int(input('Digite a opção desejada: '))

            if option == 1:
                nome = input('Digite o nome da pessoa: ')
                CPF = input('Digite o CPF da pessoa: ')
                person = Pessoa(nome, CPF)
                self.add_person(person)
            elif option == 2:
                CPF = input('Digite o CPF da pessoa: ')
                person = Pessoa(nome, CPF)
                person_found = self.find_person(person)
                if person_found:
                    print('Pessoa encontrada:')
                    print(person_found.nome)
                    print(person_found.CPF)
                    print("===================================")
                else:
                    print('Pessoa não encontrada')
            elif option == 3:
                break
            else:
                print('Opção inválida')

if __name__ == '__main__':
    app = MyApp()

print('oi')