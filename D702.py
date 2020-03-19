array1 = []
input1 = int(input())
input2 = None
for i in range(input1):
    input2 = input()
    if len(input2) == 4: #SIZE
        print(len(array1))
    elif len(input2) == 3:
        if input2 == "POP": #POP
            if len(array1) == 0:
                print("Cannot pop")
            else:
                array1.pop(0)
        elif input2 == "TOP": #TOP
            if len(array1) == 0:
                print("Empty")
            else:
                print(array1[0])
    else: #PUSH
        a, b = input2.split()
        b = int(b)
        array1.insert(0, b)
