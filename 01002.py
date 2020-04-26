import re
a = input()
b = input()
d = "(?="+b+")"

try:
	c = len(re.findall(d, a))
	print(c)
except:
	c = a.count(b)
	print(c)
