a = int(input())

b = [True] * a
c = []
cnt = 0

def k():
	global c, b, cnt
	try:
		v = b.index(True, cnt+1)
		b[v] = False
	except (IndexError,ValueError) as e:
		v = b.index(True)
		b[v] = False
	c.append(str(v+1))
	try:
		cnt = b.index(True, v+1)
	except (IndexError,ValueError) as e:
		cnt = b.index(True)

for i in range(a-2):
	k()

#need one more iter: this is with 2 left
s = b.index(True)
if s == cnt:
	b[s] = False
	c.append(str(b.index(True)+1))
	s = s + 1
else:
	c.append(str(s+1))
	s = cnt + 1

print(" ".join(c))
print(s)
