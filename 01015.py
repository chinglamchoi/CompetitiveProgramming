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

try:
    a = input()
    valid = 1
    count = 0
except:
    valid = 2
    count = 0
d = {"(":")", ")":"(", "[":"]", "]":"[", "{":"}", "}":"{"}
e = ["(", ")", "[", "]", "{", "}"]

if valid != 2:
    for i in a:
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
