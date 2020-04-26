a = int(input())
cnt = 0
msg = [""]*a

while True:
	if cnt == a:
		print("".join(msg))
		break
	b = input()
	c = int(b[3:5])
	co = int(b[5:9])
	count = 0
	b = b[9:]
	for i in b:
		count += ord(i)
	if count == co:
		msg[c-1] = b
		cnt += 1
