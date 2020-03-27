a = input()
count = 0
if a.count(",") != 5:
    print("Invalid")
else:
    b = a.split(",")
    a = 0
    for i in b:
        if b[count] == " " or b[count] == "" or b[count] == "  " or b[count] == "   " or b[count] == "    ":
            a = a + 1
        count = count + 1
    print(a)
