import math
n = input().split('$')
l = "$" + str(math.ceil(float(n[1])/2*10.0)/10.0);
print(l)
