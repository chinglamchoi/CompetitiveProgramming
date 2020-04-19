import math
x,y = input().split(" ")
x,y = int(x), int(y)

area = x*y/2 + ((x/4)**2) * math.pi
print(area)
