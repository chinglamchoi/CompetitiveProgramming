b = set({})
for i in range(int(input())):
    c = input()
    if c in b:
        b.remove(c)
        print("out")
    else:
        print("in")
        b.add(c)
