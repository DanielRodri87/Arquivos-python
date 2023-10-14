n = 0
i = 0
soma = 0

while (n >= 0):
    n = int(input())
    if n < 0:
        break
    i += 1
    soma += n
  
soma = soma/i
print(f"{soma:.2f}")

