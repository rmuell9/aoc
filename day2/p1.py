with open("assets/submit.txt", "r", encoding="utf-8") as f:
    raw_text = f.read().split(",")

res = int()

for r in raw_text:
    spl = r.split("-")

    for i in range(int(spl[0]), int(spl[1])+1):
        i = str(i)

        if len(i) % 2 == 0:
            length = int(len(i)/2)

            if i[:length] == i[length:]:
                res += int(i)
print(res)
