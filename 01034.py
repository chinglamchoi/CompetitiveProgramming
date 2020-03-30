for i in range(int(input())):
    b = input()
    if "^" in b:
        b = b.replace("^", "**")
        print(eval(b))
    else:
        print(eval(b))
