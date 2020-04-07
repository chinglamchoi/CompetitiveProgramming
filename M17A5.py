a = int(input())
b = input().split(" ")
cnt = 0
for i in b:
    if int(b[cnt]) % 2 != 0:
        print(b[cnt])
        break
    cnt = cnt + 1
if (cnt == len(b)-1) and (int(b[-1]) % 2 == 0):
    print("Goodest English")
