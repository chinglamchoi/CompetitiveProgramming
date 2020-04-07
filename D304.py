a = input()
c = ["_"] * len(a)
again = True
d = []
while again:
    if c.count("_") == 0:
        again = False
        break
    b = input()
    if b in a:
        if a.count(b) == 1:
            c[a.index(b)] = b
        else:
            f = a.index(b)
            for i in range(a.count(b)):
                c[f] = b
                try:
                    f = a.index(b, f+1)
                except ValueError:
                    break
    print(''.join(c))
        
