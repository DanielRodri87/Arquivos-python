import PySimpleGUI as sg
import random
from numpy import size

class Front:
    def tela():
        sg.theme('Dark')
        layout = [
            [sg.Frame('Sorteio', 
                [
                    [
                        sg.Text('Digite o nome dos participantes(separe por vírgulas)')
                    ],
                    [
                        sg.Input(size=(50,1), key='nome')
                    ],
                    [
                        sg.Button('Sortear', key='sortear'), sg.Button('Sair', key='sair'), sg.Button('Limpar', key='limpar')
                    ]
                ]
            )],
            [sg.Output(size=(50,1), key='saida')]
        ]
        return layout

 
    def sorteio(nome):
        nomes = nome.split(',')
        sorteado = random.choice(nomes)
        return sorteado

    def main():
        layout = Front.tela()
        janela = sg.Window('Sorteio', layout)
        while True:
            event, values = janela.read()
            if event == 'sortear':
                nome = values['nome']
                if nome == '':
                    sg.popup('Digite um nome')
                else:
                    saida = Front.sorteio(nome)
                    janela['saida'].update(saida)
            if event == sg.WIN_CLOSED or event == 'sair':
                break
            if event == 'limpar':
                janela['saida'].update('')
                janela['nome'].update('')
        janela.close()

if __name__ == '__main__':
    Front.main()