with open("assets/submit.txt", "r", encoding="utf-8") as f:
    raw_text = f.read().split("\n")[:-1]

res = int()
for l in raw_text:
    a = str()

    while len(a) != 12:
        w = len(l) - (11 - len(a))
        a += max(l[:w])
        l = l[l.index(max(l[:w]))+1:]

    res += int(a)
print(res)
