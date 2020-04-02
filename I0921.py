n, m = input().split(" ") 
ni = [] 
mi = [] 
q = []
t = 0
fullornot = []
for i in range(int(n)): 
    ni.append(int(input()))
    fullornot.append(0)
for i in range(int(m)): 
    mi.append(int(input()))
for i in range(int(m)*2):
    a = int(input())
    if a > 0:
        if 0 in fullornot:
            if len(q) == 0:
                fullornot[fullornot.index(0)] = a
            else:
                fullornot[fullornot.index(0)] = q[0]
                q.remove(q[0])
                q.append(a)
        else:
            q.append(a)
    else:
        n = fullornot.index(abs(a))
        fullornot[fullornot.index(abs(a))] = 0
        if len(q) != 0:
            fullornot[fullornot.index(0)] = q[0]
            q.remove(q[0])
        t = t + mi[abs(a)-1] * ni[n]
print(t)
