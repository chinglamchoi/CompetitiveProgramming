p = 3.1415926535897932
x,y = input().split(" ")
x,y = int(x), int(y)

area = x*y/2 + ((x/4)**2) * p
print(area)
