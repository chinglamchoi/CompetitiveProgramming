a,b,c = input().split()
a,b,c = int(a), int(b), int(c)
grid = [[0]*b for i in range(a)]
for i in range(c):
	x,y = input().split()
	x,y = int(x), int(y)
	grid[x-1][y-1] = 1
cnt, ropes, ropey, valid = 0, [], dict(), False

for i in range(a):
	if i & 1:
		count = -1
		for o in range(b):
			if grid[i][count] == 0:
				if valid == True:
					ropes[cnt-1] += 1
					ropey[cnt].append(str(i+1) + " " + str(abs(o-b)))
				else:
					cnt += 1
					ropes.append(1)
					ropey[cnt] = [str(i+1) + " " + str(abs(o-b))] #maybe x-1 faster?
					valid = True
			else:
				if valid == True:
					valid = False
			count -= 1
	else:
		for o in range(b):
			if grid[i][o] == 0:
				if valid == True:
					ropes[cnt-1] += 1
					ropey[cnt].append(str(i+1) + " " + str(o+1))
				else:
					cnt += 1
					ropes.append(1)
					ropey[cnt] = [str(i+1) + " " + str(o+1)]
					valid = True
			else:
				if valid == True:
					valid = False
print(cnt)

for i in range(cnt):
	v = ropes[i]
	print(v)
	m = i + 1
	for o in range(v):
		print(ropey[m][o])
