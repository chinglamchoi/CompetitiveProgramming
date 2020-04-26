import re
a = int(input())
y = ""
for i in range(a):
	z = input()
	b = "(>3+<)" 
	c = "("+b+")"
	d = re.findall(c, z)
	for i in d:
		y = y + i[0]
print(y.count("3"))
