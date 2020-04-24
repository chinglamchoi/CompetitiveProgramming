a = int(input())
b = {}
c = set()

d = input()
e = int(input())
c.add(e)
b[e] = d

for i in range(a-1):
	d = input()
	e = int(input())
	z = len(c)
	c.add(e)
	if len(c) != z:
		b[e] = d
	else:
		b[e] = b[e] + " " + d
b = sorted(b.items(), reverse=True)
for i in b:
	if " " not in i[1]:
		print(i[1] + " " + str(i[0]))
	else:
		z = sorted(i[1].split(" ")) #consider using .sort()
		for j in z:
			print(j + " " + str(i[0]))
