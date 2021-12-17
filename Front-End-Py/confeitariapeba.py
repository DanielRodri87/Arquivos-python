import PySimpleGUI as sg

# criar janelas e layouts
def login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Login')],
        [sg.Input()],
        [sg.Button('Continuar')]
    ]
    return sg.Window('Login', layout=layout, finalize=True)

def pedido():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Fazer Pedido')],
        [sg.Checkbox('Pizza', key='pizza'), sg.Checkbox('Bebida', key='bebida')],
        [sg.Button('Fazer pedido'), sg.Button('Voltar')]
    ]
    return sg.Window('Montar Pedido', layout=layout, finalize=True)

# criar as janelas inicias
janela1, janela2 = login(), None
# criar um loop de leitura
while True:
    window, event, values = sg.read_all_windows()
    # Quando a janela1 é fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    # Quando queremos ir para a próxima janela
    if window == janela1 and event == 'Continuar':
        janela2 = pedido()
        janela1.hide()
    if window == janela2 and event == "Voltar":
        janela1.un_hide()
        janela2.hide()
    if window == janela2 and event == "Fazer pedido":
        if values['pizza'] == True and values['bebida'] == True:
            sg.popup('Você escolheu pizza e bebida')
        elif values['pizza'] == True:
            sg.popup('Você escolheu pizza')
        elif values['bebida'] == True:
            sg.popup('Você escolheu bebida')

    # Quando queremos voltar para a janela anterior

# o que deve acontecer ao clicar nos botões


