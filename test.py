l = "234234234234278"
a = list()

while len(a) != 12:
    w = len(l) - (11 - len(a))
    a.append(max(l[:w]))
    l = l[l.index(max(l[:w]))+1:]

print(a)
