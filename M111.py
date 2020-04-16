a = list(input())
b = sorted(a)
a.sort(reverse=True)
if b[0] == "0":
	for i in range(len(a)):
		if b[i] != "0":
			c = i
			d = b[i]
			break
	b.pop(c)
	b.insert(0, d)
print("".join(a))
print("".join(b))
