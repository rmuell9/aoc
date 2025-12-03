with open("assets/submit.txt", "r", encoding="utf-8") as f:
    raw_text = f.read().split("\n")[:-1]

res = list()
for bank in raw_text:
    jolt = str()
    if bank.index(max(bank)) != len(bank)-1:
        jolt += max(bank)
        bank = bank[bank.index(max(bank))+1:]
        jolt += max(bank)
    else:
        jolt += max(bank[:-1]) + max(bank)
    res.append(int(jolt))

print(sum(res))
