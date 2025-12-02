import re

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

            else:
                twos = re.findall(r'..', i)
                if len(twos) == twos.count(twos[0]) and len(twos) > 1:
                    res += int(i)
        elif len(i) % 3 == 0:
            length = int(len(i)/3)
            if i[:length] == i[length:length*2] == i[length*2:length*3]:
                res += int(i)
        else:
            ones = re.findall(r'.', i)
            if len(ones) == ones.count(ones[0]) and len(ones) > 1:
                print(i)
                res += int(i)

print(res)
