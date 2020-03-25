a = int(input())
for i in range(a):
    b = input()
    if "^" in b:
        b = b.replace("^", "**")
        print(eval(b))
    else:
        print(eval(b))
