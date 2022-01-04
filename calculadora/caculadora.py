import PySimpleGUI as sg

layout = [
    [sg.Text('Calculadora')],
    [sg.Text('', size=(10, 1), font=("Helvetica", 25), key='-OUTPUT-')],
    [sg.InputText(size=(10, 1), key='-INPUT-')],
    [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('/')],
    [sg.Button('6'), sg.Button('5'), sg.Button('4'), sg.Button('*')],
    [sg.Button('3'), sg.Button('2'), sg.Button('1'), sg.Button('-')],
    [sg.Button('0'), sg.Button('.'), sg.Button('='), sg.Button('+')],
]
window = sg.Window('Calculadora', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == '=':
        try:
            resultado = eval(values['-INPUT-']) 
            window['-OUTPUT-'].update(resultado)
        except:
            sg.popup('Operação inválida')
    elif event == '+':
        window['-INPUT-'].update(values['-INPUT-'] + '+')
    elif event == '-':
        window['-INPUT-'].update(values['-INPUT-'] + '-')
    elif event == '*':
        window['-INPUT-'].update(values['-INPUT-'] + '*')
    elif event == '/':
        window['-INPUT-'].update(values['-INPUT-'] + '/')
    elif event == '.':
        window['-INPUT-'].update(values['-INPUT-'] + '.')
    elif event == '0':
        window['-INPUT-'].update(values['-INPUT-'] + '0')
    elif event == '1':
        window['-INPUT-'].update(values['-INPUT-'] + '1')
    elif event == '2':
        window['-INPUT-'].update(values['-INPUT-'] + '2')
    elif event == '3':
        window['-INPUT-'].update(values['-INPUT-'] + '3')
    elif event == '4':
        window['-INPUT-'].update(values['-INPUT-'] + '4')
    elif event == '5':
        window['-INPUT-'].update(values['-INPUT-'] + '5')
    elif event == '6':
        window['-INPUT-'].update(values['-INPUT-'] + '6')
    elif event == '7':
        window['-INPUT-'].update(values['-INPUT-'] + '7')
    elif event == '8':
        window['-INPUT-'].update(values['-INPUT-'] + '8')
    elif event == '9':
        window['-INPUT-'].update(values['-INPUT-'] + '9')
window.close()
