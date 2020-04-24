a = list(input())
a.insert(0, "5")

b = [["7", "8", "9"],
	 ["4", "5", "6"],
	 ["1", "2", "3"],
	 ["0", "0", "."]]
cnt = 0

def f(x):
	global b
	if x in b[0]:
		return 0
	elif x in b[1]:
		return 1
	elif x in b[2]:
		return 2
	else:
		return 3

def g(x, y):
	global b
	return b[y].index(x)

for i in range(1, len(a)):
	if a[i] != a[i-1]:
		if a[i] != "0":
			one = f(a[i])
			two = f(a[i-1]) 
			cnt = cnt + abs(one - two)
			cnt = cnt + abs(g(a[i], one) - g(a[i-1], two))
		else:
			cnt += 1
			e = f(a[i-1])
			cnt = cnt + abs(3-e)
			one = g(a[i-1], e)
			two = abs(g(a[i-1], e)-1)
			if one > two:
				cnt = cnt + two
			else:
				cnt = cnt + one
print(cnt)
