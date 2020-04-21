"""
If TLE: do calculations
"""


with open("count.in.txt", "r") as f:
	cnt = 0
	a,b = f.readline().split(" ")
	a = int(a)
	for i in range(1, a+1):
		cnt = cnt + str(i).count(b)
f.close()

with open("count.out.txt", "w") as f:
	f.write(str(cnt))
