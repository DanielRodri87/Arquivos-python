import PySimpleGUI as sg
ganho = 734
layout = [
    [
        [sg.Text('Controle de Gastos')],
        [sg.Text('', size=(100, 1), font=("Helvetica", 25), key='-OUTPUT-')],
        [sg.Text('Quanto você gastou nesse mês com funcionários?',size=(100,1), font=("Helvetica", 15))],
        [sg.InputText(size=(100, 1), key='-INPUT_FUNCIONARIOS-', default_text='0')],
        [sg.Text('Quanto você gastou nesse mês com mercadorias?',size=(100,1), font=("Helvetica", 15))],
        [sg.InputText(size=(100, 1), key='-INPUT_MERCADORIAS-', default_text='0')],
        [sg.Text('Quanto você gastou nesse mês com impostos?',size=(100,1), font=("Helvetica", 15))],
        [sg.InputText(size=(100, 1), key='-INPUT_IMPOSTOS-', default_text='0')],
        [sg.Text('Quanto você gastou nesse mês com outros custos?',size=(100,1), font=("Helvetica", 15))],
        [sg.InputText(size=(100, 1), key='-INPUT_OUTROS-', default_text='0')],
        [sg.Button('Enviar', key='-ENVIAR-', size=(30,1)), sg.Button('Exit', key='-EXIT-', size=(30,1))],
    ]
]
window = sg.Window('Controle de Gastos', layout, size=(500, 500))
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == '-EXIT-':
        break
    if event == '-ENVIAR-':
        try:
            funcionarios = float(values['-INPUT_FUNCIONARIOS-'])
            mercadorias = float(values['-INPUT_MERCADORIAS-'])
            impostos = float(values['-INPUT_IMPOSTOS-'])
            outros = float(values['-INPUT_OUTROS-'])
            total = funcionarios + mercadorias + impostos + outros
            window['-OUTPUT-'].update(total)
            window['-OUTPUT-'].update(f'Você gastou {total}')
        except ValueError:
            window['-OUTPUT-'].update('Por favor, digite apenas números.')
    if event == '-EXIT-':
        break
window.close()