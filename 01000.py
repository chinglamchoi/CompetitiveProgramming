a = int(input())
cnt = 1
for i in range(a):
	b = input() 
	b = b[0] + b[1:len(b)].replace("\" ", "UsGgRDxmCT", 1)
	b,c = b.split("UsGgRDxmCT")
	if c[0] == "C":
		c = c[5:(len(c)-1)]
		b = b + "\""
		if c in b:
			b = b.replace(c, "", 1)
	elif c[0] == "A":
		c = c[8:(len(c)-1)]
		b = b + c + "\""
	elif c[0] == "I":
		c = c[7:len(c)]
		e = c.index(" ")
		d = int(c[:e])
		c = c[(e+2):(len(c)-1)]
		b = list(b)
		b.pop(0) # is 0 one element or word?
		b.insert((d-1), c)
		b = "\"" + "".join(b) + "\""
	else:
		c = c[9:len(c)]
		e = c.index("\"")
		d = c[:e]
		c = c[(e+3):(len(c)-1)]
		if d in b:
			b = b.replace(d, c, 1)
		b = b + "\""
	b = "Command #" + str(cnt) + ": " + b 
	print(b)
	cnt = cnt + 1
