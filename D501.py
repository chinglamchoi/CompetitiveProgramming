count = 0
with open("account.txt") as file:
	a = int(file.readline())
	for i in range(a):
		b = int(file.readline())
		count = count + b
	print(count)
