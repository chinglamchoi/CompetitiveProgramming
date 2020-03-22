count = 0
a = list(input().lower())
b = list(input().lower())
if len(a) > len(b):
    print("Greater")
elif len(a) < len(b):
    print("Smaller")
else:
    for i in a:
        a[count] = ord(a[count])
        count = count + 1
    count = 0
    for k in b:
        b[count] = ord(b[count])
        count = count + 1
    count = 0
    while a[count] == b[count] and count < len(a):
        count = count + 1
    if a[count] < b[count]:
        print("Smaller")
    elif a[count] > b[count]:
        print("Greater")
    else:
        print("Equal")
