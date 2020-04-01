a = int(input())
cnt = 0
while 2 ** cnt < a or 2 ** cnt == a:
    cnt = cnt + 1
print(cnt)
