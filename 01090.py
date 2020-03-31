a = int(input())
b = []
for i in range(a):
    c = input()
    if c in b:
        b.remove(c)
        print("out")
    else:
        print("in")
        b.append(c)
