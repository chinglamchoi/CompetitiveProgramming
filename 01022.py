a = int(input())
b = {}
c = set()

d = input()
e = input()
c.add(e)
b[e] = d

for i in range(a-1):
	d = input()
	e = input()
	z = len(c)
	c.add(e)
	if len(c) != z:
		b[e] = d
	else:
		b[e] = b[e] + " " + d
b = sorted(b.items(), reverse=True)
for i in b:
	if " " not in i[1]:
		print(i[1] + " " + i[0])
	else:
		z = sorted(i[1].split(" ")) #consider using .sort()
		for j in z:
			print(j + " " + i[0])
