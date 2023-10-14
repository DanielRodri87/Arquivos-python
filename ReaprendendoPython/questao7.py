a, b, c, d = map(int, input().split())
dif = ((b*60)+d) - ((a*60)+c)
if(dif<=0):
    dif += 24*60
print(f"O JOGO DUROU {dif/60} HORA(S) E {dif%60} MINUTO(S)")
    