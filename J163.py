a = int(input())
b = input().split(" ")
input()
d = input().split(" ")
b = [int(i) for i in b]
b = sum(b)
for i in range(0, len(d)):
    if int(b - int(d[i]) * a) % 2 == 0:
        print("Robo")
    else:
        print("Alice")
