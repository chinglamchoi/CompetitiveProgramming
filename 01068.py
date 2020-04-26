a = int(input())
z = dict()
for i in range(a):
	b = input()
	c,d = b.split(" ")
	c,d = int(c), int(d)
	j = c**2+d**2
	z[j] = b
z = sorted(z.items())
for i in z:
	print(i[1])
