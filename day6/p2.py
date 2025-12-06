with open("assets/submit.txt", "r", encoding="utf-8") as f:
    raw_text = f.read().splitlines()

res = int()
ref = str()

for i in range(len(raw_text[0])-1, -1, -1):
    for row in raw_text:
        try:
            ref += row[i]
        except IndexError:
            ref += " "

ref = ref.split(" ")
op = list()

for a in ref:

    if a == "":
        continue

    if "*" in a:
        mult = 1
        a = a.strip("*")
        if a != "":
            op.append(int(a))
        for num in op:
            mult *= num

        res += mult
        op = list()

    elif "+" in a:
        a = a.strip("+")
        if a != "":
            op.append(int(a))

        res += sum(op)
        op = list()

    else:
        op.append(int(a))

print(res)
