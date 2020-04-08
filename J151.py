n,m = input().split(" ")
n,m = int(n), int(m)
a = []
cnt = 1
cnt1 = 1
a.append(str(m))
a.append(" ")
bod = 0
if n % 2 == 0:
    if (m == 0) and (n == 2):
        print("1 -1")
        bod = 1
    else:
        a.append("0")
        a.append(" ")
        for i in range(n-2):
            if cnt1 % 2 == 0:
                if cnt == m:
                    cnt = cnt + 1
                b = "-" + str(cnt)
                a.append(b)
                a.append(" ")
                cnt = cnt + 1
            else:
                if cnt == m:
                    cnt = cnt + 1
                a.append(str(cnt))
                a.append(" ")
            cnt1 = cnt1 + 1
else:
    while True:
        n = n+ 1
    if (n%2 != 0) and (m == -1):
        while True:
            n = n + 1
    else:
        foo = 0
        for i in range(n-1):
            if cnt1 % 2 == 0:
                if cnt == m:
                    cnt = cnt + 1
                b = "-" + str(cnt)
                a.append(b)
                a.append(" ")
                cnt = cnt + 1
            else:
                if cnt == m:
                    cnt = cnt + 1
                a.append(str(cnt))
                a.append(" ")
            cnt1 = cnt1 + 1
            foo = foo + 1
a.pop(-1)
if bod == 0:
    print(''.join(a))
