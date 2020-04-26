import re
a = input()
b = input()
b = "(?="+b+")"

try:
	print(len(re.findall(b, a)))
except RuntimeError:
	print(a.count(b))
