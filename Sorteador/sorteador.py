import PySimpleGUI as sg
import random

from numpy import size

class Front:
    def tela():
        sg.theme('Dark')
        layout = [
            [sg.Text('Digite o nome dos participantes(Separados por vírgula):')],
            [sg.Input(key='nome')],
            [sg.Button('Sortear')],
        
        ]
        return layout

    def sorteio(nome):
        nomes = nome.split(',')
        sorteado = random.choice(nomes)
        return sorteado

    def main():
        layout = Front.tela()
        janela = sg.Window('Sorteador', layout)
        while True:
            event, values = janela.read()
            if event == 'Sortear':
                nome = values['nome']
                sorteio = Front.sorteio(nome)
                sg.popup('O sorteado foi: {}'.format(sorteio))
                break
        janela.close()

if __name__ == '__main__':
    Front.main()