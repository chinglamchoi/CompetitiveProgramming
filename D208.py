a = int(input())
count = 0
b = input().split(" ")
for i in b:
    b[count] = int(b[count])
    count = count + 1
print(max(b))
b.remove(max(b))
print(max(b))
