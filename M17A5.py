a = int(input())
b = input().split(" ")
cnt = 0
for i in b:
    if b[cnt] % 2 != 0:
        print(b[cnt])
        break
    cnt = cnt + 1
if cnt == len(b)-1:
    print("Goodest English")
