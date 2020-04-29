a = int(input())
b = {}
c = set()
s = 0
y = []

for i in range(a):
	d = int(input())
	y.append(d)
	s += d
	z = len(c)
	c.add(d)
	if len(c) == z:
		#repeated
		b[d] += 1
	else:
		b[d] = 1
		#max(b.keys.values and output the key)

#mean
s = s/a
m = str(s)
if "." not in m:
	s = format(s, ".3f")
	#check s' vlaue + type
else:
	i, o = m.split(".")
	if (len(o) > 3) and (o[3] == "5"):
		s = str(i) + "." + o[:2] + str(int(o[2])+1)
	else:
		s = format(s, ".3f")
print(s)

#median
y.sort()
if a % 2 == 0:
	y = (y[int(a/2)] + y[int(a/2)-1])/2
	r = str(y)
	t, u = r.split(".")
	if u != "0":
		print(y)
	else:
		print(int(y))
else:
	y = y[int(a/2)]
	print(y)


#mode
print(max(b, key=b.get))
