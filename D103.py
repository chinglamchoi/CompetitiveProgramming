import math
a = int(input()) #side a 
b = int(input()) #side b
c = int(input()) #side a, b: angle
d = 1/2*a*b*math.sin(math.radians(c))
##d = float('{0:.16f}'.format(d))
print('%.3f' % d)
