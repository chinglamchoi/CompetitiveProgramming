a = input().split(" ")
a = [int(i) for i in a]

cnt = 0
if a[1] != 0:
	cnt += a[1]
if a[2] != 0:
	cnt += a[2]
if a[0] == 0:
	if a[3] != 0:
		cnt += a[3]*2
else:
	if a[3] == 0:
		cnt += int(a[0]/2)
		if a[0] % 2 != 0:
			cnt += 1
	else:
		cnt += a[3]*2
		if a[3]*2 < a[0]:
			z = a[0] - a[3]*2
			cnt += int(z/2)
			if z % 2 != 0:
				cnt += 1
print(cnt)
