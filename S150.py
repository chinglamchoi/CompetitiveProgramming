a = int(input())
b = []
cnt = 2
for i in range(1, a+1):
    for j in range(1, i+1):
        if j == 1:
            b.append(str(1))
        else:
            b.insert(0, str(int(b[cnt- 1]) + i -1))
        b.insert(0, ' ')
    b.pop(0)
    print(''.join(b))
    b = []
    cnt = 2
