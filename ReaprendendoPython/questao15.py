while True:
    altura, comp = map(int, input().split())
    if altura == 0 and comp == 0:
        break
    altb = list(map(int, input().split()))
    laser = 0
    for i in range(comp):
        if i == 0:
            if altb[i] < altura:
                laser = laser + (altura - altb[i])
        else:
            if altb[i] < altb[i - 1]:
                laser = laser + (altb[i - 1] - altb[i])
    print(laser)
    