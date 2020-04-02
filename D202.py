import functools
a = int(input())
def factors(n):
    return list(functools.reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
cnt = 0
if a != 1:
    b = factors(a)
    b.sort()
    a = []
    for i in b:
        if b[cnt] not in a:
            print(b[cnt])
            a.append(b[cnt])
        cnt = cnt + 1
else:
    print(1)
