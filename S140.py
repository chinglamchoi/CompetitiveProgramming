a = int(input())
b = []
for i in range(a):
    b.append([])
cnt = a-1
e = 0
for i in range(1, a+1):
    for j in range(1, a+1):
        if i > 1:
            b[cnt].insert(0, (str(e+i*j)))
            b[cnt].insert(0, " ")
        else:
            b[cnt].insert(0, str(j*i))
            b[cnt].insert(0, " ")
    b[cnt].pop(0)
    e = int(b[cnt][0])
    cnt = cnt - 1
cnt = 0
for i in b:
    print(''.join(b[cnt]))
    cnt = cnt + 1
    
