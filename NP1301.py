cnt = 0
with open("count.in.txt", "r") as f:
	a,b = f.readline().split(" ")
	if "\n" in b:
		b = b[:(len(b)-3)]
	a = int(a)
	for i in range(1, (a+1)):
		cnt = cnt + (str(i).count(b))
f.close()

with open("count.out.txt", "w") as f:
	f.write(str(cnt))
