a,b,c = input().split(" ")
a,b,c = float(a), int(b), int(c)
for i in range(c):
	d = str(a * b/100)
	e, f = d.split(".")
	if len(f) == 1:
		d = float(d + "0")
	elif len(f) > 2:
		d = float(e + "." + f[0] + f[1])
	else:
		d = float(d)
	a = a - d 
print("%.2f" % a)
