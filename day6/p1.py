with open("assets/submit.txt", "r", encoding="utf-8") as f:
    rows = [line.split(" ") for line in f.read().splitlines()]
    rows = [[item for item in row if item != ""] for row in rows]


res = int()
ops = rows[-1]

for j in range(len(rows[0])):
    add, mul = int(), int()

    for i in range(len(rows)-1):
        if ops[j] == "+":
            add += int(rows[i][j])
        else:
            # In case we get a column with all ones
            if mul == 0:
                mul = 1
            mul *= int(rows[i][j])

    res += add
    res += mul

print(res)
