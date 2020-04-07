again = True
b = list(map(chr, range(97, 123))) + list(map(chr, range(65, 91)))
b = b + [" "]
while again:
    try:
        cnt = 0
        a = list(input())
        for i in a:
            if a[cnt] not in b:
                a[cnt] = ""
            cnt = cnt + 1
        print(''.join(a))
    except EOFError:
        again = False
        break
