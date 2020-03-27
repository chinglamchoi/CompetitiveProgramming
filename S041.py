a = input()
b = input()
count = 0
for count in range(10):
    if int((b + str(count)))%11 == 0:
        print(count)
        break
    else:
        if count == 9:
            print(-1)
        else:
            count = count + 1
