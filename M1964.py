n,m = input().split()
n,m = int(n), int(m)
a = input().split()
b = input().split()
#subtask 1; assumes n == m

#wrong-ish cuz sometimes not first = closest

mip = dict()
mipp = set()
for i in range(m):
	if b[i] not in mipp:
		mipp.add(b[i])
		mip[b[i]] = [i]
	else:
		mip[b[i]].append(i)

cost, valid = 0, False
for i in range(n):
	try:
		for o in mip[a[i]]:
			cost += abs((i)-(int(o)))
			mip[a[i]].pop(0)
			valid = True
			break
	except KeyError:
		valid = False
	if not valid:
		print(-1)
		break
if valid:
	print(cost)
