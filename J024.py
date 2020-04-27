import statistics

a = int(input())
b = []
for i in range(a):
	b.append(int(input()))

q = statistics.mean(b)
w = statistics.median(b)
e = statistics.mode(b)

m = str(q)
if "." not in m:
	print(format(q, ".3f"))
else:
	i, o = m.split(".")
	if (len(o) > 3) and (o[3] == "5"):
		q = str(i) + "." + o[:2] + str(int(o[2])+1)
	else:
		q = format(q, ".3f")
i, o = m.split(".")

print(q)
print(w)
print(e)
