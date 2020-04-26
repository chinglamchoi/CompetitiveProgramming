b = int(input())
p = int(input())
m = int(input())


def f(b, p, m):
	if p == 1:
		return b % m

	#recursion
	r = f(b, p//2, m)
	r = r**2%m
	if (p & 1) == 1:
		#odd
		r = r*b% m
	return r
print(f(b, p, m))
