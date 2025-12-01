def rotate(x):
    if len(x) == 0:
        return 0
    return int(x.replace("R", "").replace("L", "-"))


with open("assets/submit.txt", "r", encoding="utf-8") as f:
    raw_text = f.read().split("\n")

loc, res = 50, 0

# This is not functional its just mimic a clock!

for rotation in raw_text:
    x = abs(rotate(rotation))
    s = rotate(rotation) > 0
    while x > 0:
        if s:
            loc += 1
            if loc == 100:
                res += 1
        if not s:
            loc -= 1
            if loc == 0:
                res += 1
        x-=1
        loc %= 100


print(res)
