cnt = 0
with open("count.in", "r") as f:
	a,b = f.readline().split(" ")
	a = int(a)
	for i in range(1, (a+1)):
		cnt = cnt + (str(i).count(b))
f.close()

with open("count.out", "w") as f:
	f.write(str(cnt))