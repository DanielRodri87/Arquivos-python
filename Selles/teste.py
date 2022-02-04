import PySimpleGUI as sg

class Avaliacao:
    def tela():
        sg.theme('DefaultNoMoreNagging')
        layout = [

            [sg.Text('', size=(30, 2), key='-OUTPUT-', justification='center', font=("Helvetica", 25))],

            [sg.Frame('Avalie Daniela',
                [
                    [sg.Text('Quanto mais estrelas, melhor a nota')],
                    [sg.Radio('1', 'radio', default=True), sg.Radio('2', 'radio'), sg.Radio('3', 'radio'), sg.Radio('4', 'radio'), sg.Radio('5', 'radio')],
                    [sg.Button('Enviar', key='-ENVIAR-', size=(28,1), button_color=("White", "#FF8C01")), sg.Button('Sair', key='-EXIT-', size=(28,1), button_color=("White", "#FF8C01"))],
                ], size=(300, 200)
            )],
        ]

        return sg.Window('Avaliação', layout, size=(300, 200), finalize=True)

    def main():
        janela = Avaliacao.tela()
        while True:
            event, values = janela.read()
            if event == '-ENVIAR-':
                if values[0] == '1':
                    janela['-OUTPUT-'].update('1 estrela')
                elif values[0] == '2':
                    janela['-OUTPUT-'].update('2 estrelas')
                elif values[0] == '3':
                    janela['-OUTPUT-'].update('3 estrelas')
                elif values[0] == '4':
                    janela['-OUTPUT-'].update('4 estrelas')
                elif values[0] == '5':
                    janela['-OUTPUT-'].update('5 estrelas')
                
        janela.close()

if __name__ == '__main__':
    Avaliacao.main()