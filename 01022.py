a = int(input())
rank = dict()

for i in range(a):
	b = input()
	rank[b] = int(input())

rank = sorted(rank.items(), key=lambda x: (x[1], x[0]), reverse=True)
for i in range(a):
	print(rank[i][0] + " " + str(rank[i][1]))
	# print("".join(str(rank[i])))
