a,b = input().split(" ")
d = []
e = []
cnt = 0
c = input().split(" ")
if b in c:
    print(b)
else:
    for i in c:
        d.append(abs(int(c[cnt]) - int(b)))
        cnt = cnt + 1
    if d.count(min(d)) == 1:
        print(c[d.index(min(d))])
    else:
        cnt = 0
        for i in range(d.count(min(d))):
            e.append(c[d.index(min(d), cnt)])
            cnt = d.index(min(d), cnt) + 1
        e.sort()
        print(e[len(e) - 1])
