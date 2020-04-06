a = int(input())
b = []
cnt = 0
for j in range(1, a+1):
    for i in range(j**2, j**2+a):
        if cnt == 0:
            b.append(str(i))
        else:
            b.append(str(int(d) + j))
        d = b[cnt]
        b.append(" ")
        cnt = cnt + 2
    b.pop(-1)
    print(''.join(b))
    cnt = 0
    b = []
