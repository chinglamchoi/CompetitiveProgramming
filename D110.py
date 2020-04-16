a, b = list(input())
c, d = list(input())
b, d = int(b), int(d)
dictt = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}
a, c = dictt[a], dictt[c]
r1 = abs(d-b)
r2 = abs(c-a)
if r1 > r2:
	print(r1)
else:
	print(r2)
