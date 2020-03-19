array1 = []
input1 = int(input())
input2 = None
for i in range(input1):
    input2 = input()
    if len(input2) == 4:
        print(len(array1))
    elif len(input2) == 5:
        if len(array1) == 0:
            print("Empty")
        else:
            print(array1[len(array1) - 1])
    elif len(input2) == 3:
        if len(array1) == 0:
            print("Cannot pop")
        else:
            array1 = [array1.pop(0)]
    else:
        a, b = input2.split()
        b = int(b)
        array1.insert(0, b)
