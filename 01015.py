#use stack because lifo
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if len(self.items) != 0:
            return self.items.pop()

    def peek(self):
        if len(self.items) != 0:
            return self.items[-1]
        else:
            return "Nope"

S = Stack()

a = input()
d = {"(":")", ")":"(", "[":"]", "]":"[", "{":"}", "}":"{"}
e = ["(", ")", "[", "]", "{", "}"]

count = 0
valid = 1

for i in a:
    # if len(a) % 2 != 0:

    #     valid = 0
    #     break
    # else:
    if i in e:
        if i == "(" or i == "[" or i == "{":
            S.push(i) #tried: clear
            count += 1
        else:
            if count == 0:
                valid = 0
                break
            else:
                if S.peek() != d[i]: #clear
                    valid = 0
                    break
                else:
                    S.pop() #clear
                    count -= 1

if valid == 0 or count != 0:
    print("No") #Change for HKOI
else:
    print("Yes")

"""
Test Cases:
((, ], [(]), )(
"""
