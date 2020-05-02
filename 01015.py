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

a = input() #.replace(" ", "")
d = {"(":")", ")":"(", "[":"]", "]":"[", "{":"}", "}":"{"}

count = 0
valid = 1

for i in a:
    if len(a) % 2 != 0:
        valid = 0
        break
    else:
        if i == "(" or i == "[" or i == "{":
            S.push(i)
            count += 1
        else:
            if count == 0:
                valid = 0
                break
            else:
                if S.peek() != d[i]:
                    valid = 0
                    break
                else:
                    S.pop()
                    count -= 1

if valid == 0 or count != 0:
    print("No")
else:
    print("Yes")
