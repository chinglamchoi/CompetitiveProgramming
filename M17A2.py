c = 0
count = 0
e = [0]
a = int(input())
b = input().split(" ")
for i in b:
    if e.count(int(b[count])) == 0:
        e.append(int(b[count]))
    count = count + 1
count = 0
for k in e:
    c = c + e[count]
    count = count + 1
print(c)
