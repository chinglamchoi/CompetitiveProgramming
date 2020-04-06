a = []
for i in range(int(input())):
    a.append(int(input()))
a.sort()
b = 0
cnt = 0
while len(a) != 1:
    if len(a) == 1:
        b = b + a[cnt]
        break
    c = a[cnt] + a[cnt+1]
    b = b + c
    a.pop(cnt)
    a.pop(cnt)
    a.insert(0, c)
    a.sort()
print(b)
