maior = 0
num = []
a, b, c = map(int, input().split())
num.append(a)
num.append(b)
num.append(c)
for i in range(3):    
    if maior < num[i]:
        maior = num[i]
        
    
print(f"{maior} eh o maior")