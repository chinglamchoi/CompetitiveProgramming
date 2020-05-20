a = int(input())
b = input().split()
r1 = [b[0]]
r2 = []
p = "1"
valid = 1

for i in range(1, a):
	if int(b[i]) < int(r1[-1]):
		if (len(r2) == 0) or (int(b[i]) > int(r2[-1])):
			r2.append(b[i])
			p = p + " " + "2"
		else:
			valid = 0
			break
	else:
		r1.append(b[i])
		p = p + " " + "1"

if valid == 0:
	print("NO")
else:
	print("YES")
	print(p)
