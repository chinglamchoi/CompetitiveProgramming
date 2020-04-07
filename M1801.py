a = input().split(" ")
b = input().split(" ")
if ("9" in a) and ("6" not in a):
    a.append("6")
elif ("6" in a) and ("9" not in a):
    a.append("9")
if ("9" in b) and ("6" not in b):
    b.append("6")
elif ("6" in b) and ("9" not in b):
    b.append("9")
for i in range(int(input())):
    c = input()
    if ((c[0] in a) and (c[1] in b)) or ((c[0] in b) and (c[1] in a)):
        print("Yes")
    else:
        print("No")
