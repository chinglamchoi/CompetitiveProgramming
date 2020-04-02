a = input()
a = a.replace(" ", "")
e = 0
def st(a):
    global e
    eg = ["23456789"]
    a = list(a)
    a.sort()
    if ((''.join(a) in eg) or (''.join(a) == "2345A") or (''.join(a) == "6789T") or (''.join(a) == "AJKQT") or (''.join(a) == "89JQT") or (''.join(a) == "789JT") or (''.join(a) == "9JKQT")):
        e = e + 0.1

def fof(a):
    global e
    b = []
    cnt = 0
    for i in a:
        b.append(a.count(a[cnt]))
        cnt = cnt + 1
    if (2 in b) and (3 in b):
        e = e + 0.5
    elif 4 in b:
        e = e + 1.1
    
if (a.count("D") == 5) or (a.count("C") == 5) or (a.count("H") == 5) or (a.count("S") == 5):
    e = 0.3
a = ''.join(a)
a = a.replace("D", "")
a = a.replace("C", "")
a = a.replace("H", "")
a = a.replace("S", "")
st(a)
fof(a)
if e == 0:
    print(0)
elif e == 0.1:
    print(1)
elif e == 0.3:
    print(2)
elif e == 0.5:
    print(3)
elif e == (1.1):
    print(4)
else:
    print(5)
