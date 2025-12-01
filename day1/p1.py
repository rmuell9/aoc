def rotate(x):
    return int(x.replace("R", "").replace("L", "-"))


with open("assets/submit.txt", "r", encoding="utf-8") as f:
    raw_text = f.read().split("\n")[:-1]

loc, res = 50, 0

for rotation in raw_text:
    loc = (loc + rotate(rotation)) % 100
    if loc == 0:
        res += 1

print(res)
