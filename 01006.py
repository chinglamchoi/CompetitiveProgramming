a = int(input())
b = int(input())
d = 0
for i in range(b):
    c = int(input())
    a = a - c
    if a > 0:
        a = a 
    elif a <= 0:
        a = a + 250
        d = d+250
print("$" + str(d).strip())
