a, b, c = map(float, input().split())

delta = (b ** 2) - (4 * a * c)
if delta < 1:
    print('Impossivel calcular')
else:
    r1 = (-b + (delta ** 0.5)) / (2 * a)
    r2 = (-b - (delta ** 0.5)) / (2 * a)
    print('R1 = {:.5f}'.format(r1))
    print('R1 = {:.5f}'.format(r2))
