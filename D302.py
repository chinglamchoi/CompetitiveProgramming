a = input()
print(len(list(a)))
a = a.split(" ")
count = 0
cnt = 0
for i in a:
    if a[count] != "," and a[count] != "." and a[count] != "!" and a[count] != "?":
        cnt = cnt + 1
    count = count + 1
print(cnt)
