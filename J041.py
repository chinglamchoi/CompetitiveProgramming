from math import gcd

a = int(input())
d = []

for i in range(a):
	b,c = input().split(" ")
	d.append(int(b)+int(c))
lcm = d[0]

for i in d[1:]:
	lcm = lcm*i//gcd(lcm, i)

print(lcm)
