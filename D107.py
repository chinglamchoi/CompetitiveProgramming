import math
a = int(input())
if a == 1:
    while True:
        a = a + 1
def is_int(s):
    if s % 1 == 0:
        return True
    else:
        return False
    

if (is_int(math.sqrt(a)) == True) and (is_int(math.sqrt(8*a+1)) == True): 
    print("Both")
elif (is_int(math.sqrt(a)) == True) and (is_int(math.sqrt(8*a+1)) == False):
    print("Square")
elif (is_int(math.sqrt(8*a+1)) == True) and (is_int(math.sqrt(a)) == False):
    print("Triangular")
else:
    print("Neither")

#Doesn't work for second to last case
