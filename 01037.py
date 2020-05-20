import itertools as it
a,b,c = input().split()
a,b,c = int(a), int(b), int(c)
d = "".join(sorted(list(input())))
prin = list(it.combinations(d, b))
count = []
cnt = 0
valid = set()
x = 0
for i in prin:
	if cnt == c:
		break
	valid.add(i)
	y = len(valid)
	if y != x:
		print("".join(i))
		cnt += 1
	x = y
