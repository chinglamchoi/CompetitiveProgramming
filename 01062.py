a,b = input().split(" ")
d, e = a.lower(), b.lower()
c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
d = "".join([i for i in d if i in c])
e = "".join([i for i in e if i in c])
if d > e:
	print(a + " is greater than " + b)
elif d < e:
	print(a + " is less than " + b)
else:
	print(a + " is equal to " + b)
