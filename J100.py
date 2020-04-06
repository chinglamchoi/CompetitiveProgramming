a = int(input())
cnt = 1
b = []
for i in range(1, a+1):
    for j in range(i):
        b.append(str(cnt))
        b.append(" ")
        cnt = cnt + 1
    b.pop(-1)
    print(''.join(b))
    b = []
b = []
for i in range(a-1, 0, -1):
    for j in range(i):
        b.append(str(cnt))
        b.append(" ")
        cnt = cnt + 1
    b.pop(-1)
    print(''.join(b))
    b = []
