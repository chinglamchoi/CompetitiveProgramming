a = input()
b = input()
c = int(a) - int(b)
if len(b) >= len(a):
    d = "-" + b
    e = " " * (len(d)-len(a)) + a
    print(e)
    print(d)
    d = "-" * len(d)
    print(d)
else:
    d = "-" + b
    d = "-" + " " * (len(a) - len(d)+1) + b
    e = len(d)
    e = " " * (len(d)-len(a)) + a
    print(e)
    print(d)
    d = "-" * len(d)
    print(d)
if c >= 0:
    e = " " * (len(d)-len(str(c))) + str(c)
    print(e)
else:
    c = "-" + str(abs(int(a)-int(b)))
    d = "-" + " " * (len(d) - len(c)) + str(abs(int(a) - int(b)))
    print(d)
