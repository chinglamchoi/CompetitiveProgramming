from math import gcd

a = int(input())
d = []
b,c = input().split(" ")
lcm = int(b) + int(c)

for i in range(a-1):
	b,c = input().split(" ")
	d.append(int(b)+int(c))

for i in range(1, a-1):
	lcm = lcm*d[i]//gcd(lcm, d[i])

print(lcm)
