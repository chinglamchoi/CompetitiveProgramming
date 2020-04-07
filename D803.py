p = int(input())
a = input().split(" ")
a = [int(i) for i in a]
b = []
cnt = 0
#iterating over a
for i in a:
    j = a.index(i)
    #i is not the first element
    while j>0:
        #not in order
        if a[j-1] > a[j]:
            #swap
            a[j-1],a[j] = a[j],a[j-1]
        else:
            #in order
            break
        j = j-1
    for z in range(0, cnt+1):
        b.append(str(a[z]))
        b.append(" ")
    b.pop(len(b)-1)
    print(''.join(b))
    cnt = cnt + 1
    b = []
