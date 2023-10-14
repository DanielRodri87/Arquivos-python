n = int(input())

for i in range(n):
    numero = input()
    leds = 0
    for j in numero:
        if j == '1':
            leds += 2
        elif j == '2' or j == '3' or j == '5':
            leds += 5
        elif j == '4':
            leds += 4
        elif j == '6' or j == '9' or j == '0':
            leds += 6
        elif j == '7':
            leds += 3
        elif j == '8':
            leds += 7
    print(leds, 'leds')