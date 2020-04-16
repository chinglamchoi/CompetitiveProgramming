with open("weather.txt") as file:
	e = []
	cnt = 0
	d = [str(i) for i in range(0, 10)]
	for i in file:
		b = list(i)
		f = "".join(b)
		if len(b) > 1:
			cnt = -11
			again = True
			c = str()
			if ("degrees" not in f) or ("." in f):
				cnt = -10
			while again:
				if b[cnt] not in d:
					again = False
					break
				if b[cnt] in d:
					c = b[cnt] + c
					cnt = cnt - 1
			e.append(int(c))
	print(str(min(e)) + " " + str(max(e)))
