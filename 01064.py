a = int(input())
b = []
c = {}
for i in range(a):
	d = input()
	if d not in c:
		c[d] = 1
	else:
		c[d] = c[d] + 1
p = []
d = max(c.values())
for i in c:
	if c[i] == d:
		p.append(i)
p.sort()
for i in p:
	print(i)
