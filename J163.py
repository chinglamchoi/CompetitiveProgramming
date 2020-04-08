a = int(input())
b = input().split(" ")
c = int(input())
d = input().split(" ")
for i in range(0, len(d)):
    count = 0
    for j in range(0, len(b)):
        if b[j] != d[i]:
            if int(b[j]) > int(d[i]):
                count = count + int(b[j]) - int(d[i])
            else:
                count = count + int(d[i]) - int(b[j])
    if count == 0:
        print("Robo")
    else:
        if count % 2 == 0:
            print("Robo")
        else:
            print("Alice")
        
