from pytube import YouTube
while True:
    print()
    print('='*60)
    print('Baixe qualquer música com a melhor qualidade possível! ')
    print('='*60)

    url = str(input('Cole aqui o link de um vídeo: '))
    local = "C:\\Users\\Rodrigues\\Desktop\\"
    informacoes = YouTube(url)

    print('=========== INFORMAÇÕES DO VÍDEO LINKADO ===========\n')
    print('Título: ',informacoes.title, '\n')
    print('Tamanho da música: {:.2} minuto(s)'.format(informacoes.length/60))
    print('O seu vídeo tem: ', informacoes.views, 'visualizações \n' )
    
    resolucao = informacoes.streams.get_audio_only()

    print('Seu vídeo está sendo baixado... ')
    resolucao.download(local)
    print('Download completo, seja feliz')

    input('clique em qualquer letra para sair: ')
    break