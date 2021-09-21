

size = float(input("Insira o tamanho do arquivo que irá baixar (MB): "))
link = float(input("Insira a velocidade do seu link de internet (Mbps): "))

time = size / (link / 8)

print(f"Seu download demorará {time/60:.2f} minutos.")