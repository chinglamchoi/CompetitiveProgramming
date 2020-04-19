a = int(input())
b = 1
count = 0
continuee = True
while continuee:
	add = (a+1) // (2*b)*b
	count = count + add
	if (a+1) > b: #valid
		add = (a+1) % (2*b)
		if add > b:
			count = count + (add-b)
	b = b*2 #inc
	if (a+1) < b:
		continuee = False
print(count)
