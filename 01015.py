#use stack because lifo
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]

S = Stack()

a = input().replace(" ", "")
d = {"(":")", ")":"(", "[":"]", "]":"[", "{":"}", "}":"{"}

valid = 1

for i in a:
    if i == "(" or i == "[" or i == "{":
        S.push(i)
    else:
        if S.peek() != d[i]:
            valid = 0
            print("No")
            break
        else:
            S.pop()

if valid == 1:
    print("Yes")
