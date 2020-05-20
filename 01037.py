import itertools as it
a,b,c = input().split()
a,b,c = int(a), int(b), int(c)
d = "".join(sorted(list(input())))
prin = list(it.combinations(d, b))
count = []
cnt = 0
for i in prin:
	if cnt == c:
		break
	if i not in count:
		print("".join(i))
		count.append(i)
		cnt += 1
