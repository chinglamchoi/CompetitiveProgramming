while True:
    a,b = input().split(" ")
    a = int(a)
    b = int(b)
    c = input()
    d = input()
    if c == "IST":
        while True:
            c = c + 1
    if c == "PST":
        a = a + 8
    elif c == "MST":
        a = a + 7
    elif c == "EST":
        a = a + 5
    elif c == "ACDT":
        a = a - 10
        b = b - 30
    elif c == "MSK":
        a = a - 3
    elif c == "IST":
        a = a - 5
        b = b - 30
    elif c == "NPT":
        a = a - 5
        b = b - 45
    elif c == "HKT":
        a = a - 8
    elif c == "JST":
        a = a - 9


    if d == "PST":
        a = a - 8
    elif d == "MST":
        a = a - 7
    elif d == "EST":
        a = a - 5
    elif d == "ACDT":
        a = a + 10
        b = b + 30
    elif d == "MSK":
        a = a + 3
    elif d == "IST":
        a = a + 5
        b = b + 30
    elif d == "NPT":
        a = a + 5
        b = b + 45
    elif d == "HKT":
        a = a + 8
    elif d == "JST":
        a = a + 9
    d = []
    c = 0
    d.append(" ")
    if b in range(0, 60):
        if b >= 10:
                d.append(str(b))
        else:
            b = "0" + str(b)
            d.append(b)
    else:
        if b < 0:
            b = 60 + b
            c = c -1
            if b >= 10:
                d.append(str(b))
            else:
                b = "0" + str(b)
                d.append(b)
        elif b > 59:
            b = b - 60
            c = c + 1
            if b >= 10:
                d.append(str(b))
            else:
                print("hye")
                print(b)
                b = "0" + str(b)
                d.append(b)

    a = a + c
    if a in range(0, 24):
        if a >= 10:
            d.insert(0,str(a))
        else:
            a = "0" + str(a)
            d.insert(0,a)
    else:
        if a < 0:
            a = 24 + a
            if a >= 10:
                d.insert(0,str(a))
            else:
                a = "0" + str(a)
                d.insert(0,a)
        elif a > 23:
            a = a - 24
            if a >= 10:
                d.insert(0,str(a))
            else:
                a = "0" + str(a)
                d.insert(0, a)
    print(''.join(d))
