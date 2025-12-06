with open("assets/submit.txt", "r", encoding="utf-8") as f:
    rowz = [list(line) for line in f.read().splitlines()]


def removable(rows):
    res = int()

    for r in range(len(rows)):
        for c in range(len(rows[0])):
            nearby = int()

            if rows[r][c] != "@":
                continue
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    cc = c + dx
                    rr = r + dy

                    if 0 <= rr < len(rows) and 0 <= cc < len(rows[0]):
                        nearby += rows[rr][cc] == "@"

            if nearby < 4:
                res += 1
                rows[r][c] = "x"

    return rows, res


ans = int()

x = removable(rowz)
while x[1] != 0:
    ans += x[1]
    x = removable(x[0])

print(ans)
