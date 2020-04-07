a = input().split(" ")
b = input().split(" ")
for i in range(int(input())):
    c = list(input())
    if (c[0] in a) and (c[1] in b):
        print("Yes")
    elif (c[0] in b) and (c[1] in a):
        print("Yes")
    else:
        if ((c[0] == "9") and ("6" in a)) or ((c[0] == "6") and ("9" in a)):
            if c[1] in b:
                print("Yes")
            elif ((c[1] == "9") and ("6" in b)) or ((c[1] == "6") and ("9" in b)):
                print("Yes")
            else:
                print("No")
        elif ((c[1] == "9") and ("6" in a)) or ((c[0] == "6") and ("9" in a)):
            if c[0] in b:
                print("Yes")
            elif ((c[0] == "9") and ("6" in b)) or ((c[1] == "6") and ("9" in b)):
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    
