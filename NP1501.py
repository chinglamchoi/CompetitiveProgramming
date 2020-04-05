with open("coin.in", "r") as a:
    b = int(a.read())
    cnt = 1
    d = 0
    s = 0
    while d < b:
        for i in range(cnt):
            if d >= b:
                break
            s = s + cnt
            d = d + 1
        cnt = cnt + 1
with open("coin.out", "w") as a:
    a.write(str(s))
