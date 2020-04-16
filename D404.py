a = int(input())
b = []
for i in range(a):
	b.append(input().split(" "))
c = int(input())
for i in range(c):
	d,e,f = input().split(" ")
	d,e = int(d), int(e)
	if f == "A":
		if d < e:
			print(b[d-1][e-1])
		else:
			print(b[e-1][d-1])
	else:
		if d > e:
			print(b[d-1][e-1])
		else:
			print(b[e-1][d-1])
