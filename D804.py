a,b = input().split(" ")
a,b = int(a), int(b)

c = input().split(" ")
d = input().split(" ")

c = c + d
c = sorted([int(i) for i in c])
d = " ".join([str(i) for i in c])
print(d)
