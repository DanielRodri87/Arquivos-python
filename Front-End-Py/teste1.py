import PySimpleGUI as sg
class Tela:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Nome:'), sg.InputText()],
            [sg.Text('Idade:'), sg.InputText()],
            [sg.Button('Ok')]
        ]
        # JanelA
        janela = sg.Window('Dados dos usuários').Layout(layout)
        # Extrair dados da tela
        self.button, self.values = janela.Read()

    def iniciar(self):
        print(self.values)

tela = Tela()
tela.iniciar()