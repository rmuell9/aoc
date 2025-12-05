with open("assets/submit.txt", "r", encoding="utf-8") as f:
    raw_text = f.read().split("\n\n")
    ranges = raw_text[0].splitlines()
    tests = raw_text[1].splitlines()

inrange = list()
for item in ranges:
    bounds = item.split("-")

    for test in tests:
        if int(test) >= int(bounds[0]) and\
                int(test) <= int(bounds[1]) and\
                test not in inrange:
            inrange.append(test)

print(len(inrange))
