a = int(input())
z = a
b = []
c = 2
while (c*c <= a):
    if (a % c == 0):
        a = a // c
        b.append(str(c))
    else: 
        c += 1
if (a != 1):
    b.append(str(a))
print(str(z)+"="+"*".join(b))
