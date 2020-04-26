import re
a = input()
b = input()
b = "(?="+b+")"

print(len(re.findall(b, a)))
