a,b,c = input().split(" ")
bscore = 0
bscore1 = 0
cscore = 0
cscore1 = 0
for i in range(0, 6):
    if i >= 2:
        if b[i] != a[i]:
            bscore = bscore + 1
            bscore1 = bscore1 + abs(int(b[i]) - int(a[i]))
        if c[i] != a[i]:
            cscore = cscore + 1
            cscore1 = cscore1 + abs(int(c[i]) - int(a[i]))
    else:
        if b[i] != a[i]:
            bscore = bscore + 1
            bscore1 = bscore1 + abs(ord(b[i]) - ord(a[i]))
        if c[i] != a[i]:
            cscore = cscore + 1
            cscore1 = cscore1 + abs(ord(c[i]) - ord(a[i]))
if bscore < cscore:
    print(b)
elif bscore == cscore:
    print(b, c)
else:
    print(c)
