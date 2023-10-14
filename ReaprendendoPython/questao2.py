# 1113

while True:
    x, y = map(int, input().split())
    if x == y:
        break
    elif x > y:
        print("Decrescente")
    elif x < y:
        print("Crescente")
        
