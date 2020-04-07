a = input()
c = ["_"] * len(a)
while True:
    if c.count("_") == 0:
        break
    b = input()
    if b in a:
        if a.count(b) == 1:
            c[a.index(b)] = b
        else:
            f = a.index(b)
            e = a.count(b)
            for i in range(1, e+1): 
                c[f] = b
                if i == e:
                    break
                f = a.index(b, f+1)
    print(''.join(c))
