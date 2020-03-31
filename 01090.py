a = int(input())
b = []
for i in range(a):
    c = input()
    b.append(c)
    if b.count(c) % 2 == 0:
        print("out")
    else:
        print("in")
