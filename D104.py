import math as m

a,b,c = input().split(" ")
a,b,c = int(x), int(y), int(z)

d = b**2-4*a*c
if d < 0:
    print("None")
elif d == 0:
    d = format(((-b+m.sqrt(b**2-4*a*c))/2*a), ".3f")
else:
    d = format(((-b+m.sqrt(b**2-4*a*c))/2*a), ".3f")
    e = format(((-b-m.sqrt(b**2-4*a*c))/2*a), ".3f")
    if d > e:
        print(str(e) + " " + str(d))
    else:
        print(str(d) + " " + str(e))
