with open("assets/submit.txt", "r", encoding="utf-8") as f:
    rows = f.read().splitlines()

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
        res += nearby < 4

print(res)
