import re
a = input()
b = input()
try:
	b = "(?="+b+")"
except RuntimeError:
	while True:
		c = 1
# try:
# 	print(len(re.findall(b, a)))
# except RuntimeError:
# 	print(a.count(b))
