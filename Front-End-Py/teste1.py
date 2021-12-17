import PySimpleGUI as sg

# class Tela:
#     def __init__(self):
#         # Layout
#         layout = [
#             [sg.Text('Nome:'), sg.InputText()],
#             [sg.Text('Idade:'), sg.InputText()],
#             [sg.Button('Ok')]
#         ]
#         # JanelA
#         janela = sg.Window('Dados dos usuários').Layout(layout)
#         # Extrair dados da tela
#         self.button, self.values = janela.Read()

#     def iniciar(self):
#         print(self.values)

# tela = Tela()
# tela.iniciar()

class Bar_do_Daniel:
    def __init__(self):
        sg.change_look_and_feel('Dark')
        # Layout
        layout = [
            [sg.Text('Nome:', size=(5,0)), sg.InputText(size=(20,0),key='nome')],
            [sg.Text('Idade:', size=(5,0)), sg.InputText(size=(20,0),key='idade')],
            [sg.Text('Bebida', size=(5,0)), sg.InputText(size=(20,0),key='bebida')],
            [sg.Text("Aceita cartão?")],
            [sg.Radio('Sim', 'cartoes',key="aceita"), sg.Radio('Não', 'cartoes',key="rejeita")],
            [sg.Text('Quais provedores são aceitos?')],
            [sg.Checkbox('Gmail',key="gmail"), sg.Checkbox('Facebook',key='facebook')], 
            [sg.Slider(range=(0,100), default_value=0, orientation='h', size=(20,20), key='slider')],
            [sg.Button('Ok')],
            [sg.Output(size=(30,10))]
        ]
        # Janela
        self.janela = sg.Window('Bar do Daniel').Layout(layout)

        # Extrair dados da tela
        self.button, self.values = self.janela.Read()

    def iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            bebida = self.values['bebida']
            gmail = self.values['gmail']
            facebook = self.values['facebook']
            aceita = self.values['aceita']
            rejeita = self.values['rejeita']
            velocidade = self.values['slider']

            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Bebida: {bebida}')
            print(f'Gmail: {gmail}')
            print(f'Facebook: {facebook}')
            print(f'Aceita cartão: {aceita}')
            print(f'Rejeita cartão: {rejeita}')  
            print(f'Velocidade: {velocidade}')  
bar = Bar_do_Daniel()
bar.iniciar()

