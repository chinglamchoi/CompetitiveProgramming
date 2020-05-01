a = input().split(" ")
cnt = 0
if a[1] != "0":
	cnt += int(a[1])
if a[2] != "0":
	cnt += int(a[2])
if a[0] == "0":
	if a[3] != "0":
		cnt += int(a[3])*2
else:
	if a[3] == "0":
		cnt += int(int(a[0])/2)
		if int(a[0]) % 2 != 0:
			cnt += 1
	else:
		cnt += int(a[3])
		if int(a[3]) < int(a[0]):
			z = int(a[0]) - int(a[3])
			cnt += int(z/2)
			if z % 2 != 0:
				cnt += 1
print(cnt)
