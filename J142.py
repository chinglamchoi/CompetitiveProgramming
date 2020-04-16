overall, sl, bl, sm, bm = 0, 0, 0, 0, 0

a = int(input())
for i in range(a):
	b = input()
	if b[0] != "4":
		b,c = b.split(" ")
		c = int(c)
		if b == "1":
			bl = bl + c
			bm = bm + c
			overall = overall + c
		elif b == "2":
			sl = sl + c
			sm = sm + c
			overall = overall + c
		else:
			overall = overall - c
			#least first
			if bl > c:
				bl = bl - c
			elif bl == c:
				bl = 0
			else:
				sl = sl - (c - bl)
				bl = 0
			#max
			if sm > c:
				sm = sm - c
			elif sm == c:
				sm = 0
			else:
				bm = bm - (c -sm)
				sm = 0			
	else:
		print(str(bm) + " " + str(bl))
