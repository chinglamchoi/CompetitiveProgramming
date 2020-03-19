a, b, c = input().split(" ")
d, e, f = input().split(" ")
if a > d:
    print("After")
elif a == d:
    if b > e:
        print("After")
    elif b == e:
        if c > f:
            print("After")
        elif c==f:
            print("Same")
        else:
            print("Before")
    else:
        print("Before")
else:
    print("Before")
