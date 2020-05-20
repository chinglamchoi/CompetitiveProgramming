import itertools as it
a,b,c = input().split()
a,b,c = int(a), int(b), int(c)
d = list(input())
d.sort()
d = "".join(d)
prin = list(it.combinations(d, b))
foo = ["@"]
cnt = 0
for i in prin:
	if cnt == c:
		break
	if i != foo[-1]:
	#check if triggers index error
		print("".join(i))
		foo.append(i)
		cnt += 1
