num = int(input())

a = input().split()
b = input().split()
a = [int(i) for i in a]
b = [int(i) for i in b]
a.sort()
b.sort()

if a[0] > b[-1]:
	print(num)
elif a[-1] < b[0]:
	print("0")
else:
	if (num == 1) and (a == b):
		print("0")
	else:
		wins = 0
		cnt = 0
		valid = True
		for i in range(num):
			valid = True
			if cnt == num:
				break
			while (a[cnt] <= b[i]) and (cnt < num):
				cnt += 1
				if cnt == num:
				    valid = False
				    break
				elif (cnt == num-1) and (a[cnt] <= b[i]):
					valid = False
					break
			if valid == False:
				break
			else:
				wins += 1
			cnt += 1
		print(wins)
