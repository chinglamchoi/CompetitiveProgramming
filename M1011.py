a = input().split(' ')
c = []
e = []
d = dict()
for i in a:
  try:
    b = int(i)
    if b not in e:
      e.append(b)
      b = int(i[0])
      if b in c:
        d[b] = d[b] + 1
      else:
        c.append(b)
        d[b] = 1
  except (ValueError, IndexError):
    pass
c.sort()
for i in c:
    e = str()
    e = str(i) + " " + str(d[i])
    print(e)
