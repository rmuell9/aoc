with open("assets/submit.txt", "r", encoding="utf-8") as f:
    rows = [list(line) for line in f.read().splitlines()]

res = int()


def manifolds(i, j):
    global res
    for k in range(i+1, len(rows)):
        if rows[k][j] == "|":
            break
        elif rows[k][j] != "^":
            rows[k][j] = "|"
            continue
        res += 1
        manifolds(k, j+1)
        manifolds(k, j-1)
        break


start = rows[0].index("S")
manifolds(0, start)

print(res)
