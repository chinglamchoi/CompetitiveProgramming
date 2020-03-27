a = int(input())
b = a
while b > 0:
    if b >= 1000:
        print(1000)
        b = b - 1000
    elif b >= 500:
        print(500)
        b = b - 500
    elif b >= 100:
        print(100)
        b = b - 100
    elif b >= 50:
        print(50)
        b = b - 50
    elif b >= 20:
        print(20)
        b = b - 20
    elif b >= 10:
        print(10)
        b = b - 10
