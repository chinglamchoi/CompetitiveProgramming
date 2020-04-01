b = []
cnt = 0
for i in range(3):
    a = input()
    for i in a:
        b.append(a[cnt])
        cnt += 1
    cnt = 0
if b.count("X") < 3 and b.count("O") < 3:
    print("Not ended")
else:
    if not((b[0] == b[1] == b[2]) or (b[3] == b[4] == b[5]) or (b[6] == b[7] == b[8]) or (b[0] == b[3] == b[6])
                                 or (b[1] == b[4] == b[7]) or (b[2] == b[5] == b[8]) or (b[0] == b[4] == b[8]) or (b[2] == b[4] == b[6])):
        if b.count(".") == 0:
            print("Draw")
        else:
            print("Not ended")
    else:
        if (b[0] == b[1] == b[2] == "X") or (b[3] == b[4] == b[5] == "X") or (b[6] == b[7] == b[8] == "X") or (b[0] == b[3] == b[6] == "X") or (b[1] == b[4] == b[7] == "X") or (b[2] == b[5] == b[8] == "X") or (b[0] == b[4] == b[8] == "X") or (b[2] == b[4] == b[6] == "X"):
            print("X wins")
        elif (b[0] == b[1] == b[2] == "O") or (b[3] == b[4] == b[5] == "O") or (b[6] == b[7] == b[8] == "O") or (b[0] == b[3] == b[6] == "O") or (b[1] == b[4] == b[7] == "O") or (b[2] == b[5] == b[8] == "O") or (b[0] == b[4] == b[8] == "O") or (b[2] == b[4] == b[6] == "O"):
            print("O wins")
        else:
            print("Not ended")
