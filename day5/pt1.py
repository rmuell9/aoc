with open("assets/submit.txt", "r", encoding="utf-8") as f:
    raw_text = f.read().split("\n\n")
    ranges = [(int(low), int(high)) for (low, high) in
              [range.split("-") for range in raw_text[0].splitlines()]]
    tests = [int(test) for test in raw_text[1].splitlines()]

inrange = set()
for low, high in ranges:
    for test in tests:
        if low <= test <= high:
            inrange.add(test)

print(len(inrange))
