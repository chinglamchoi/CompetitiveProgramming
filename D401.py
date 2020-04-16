a = int(input())
b = [True]*(a+1)

#b[0] and b[1] should be ignored
c = int(a**(.5))+1
for i in range(2, c):
	if b[i]:
		count = 0
		cnt = 0
		while cnt < a:
			cnt = i**2+count*i
			if cnt > a:
				break
			else:
				b[cnt] = False
				count = count + 1 
for i in range(2, len(b)):
	if b[i]:
		print(i)
