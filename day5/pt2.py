with open("assets/submit.txt", "r", encoding="utf-8") as f:
    raw_text = f.read().split("\n\n")
    ranges = raw_text[0].splitlines()

for i in range(len(ranges)):
    bounds = ranges[i].split("-")
    ranges[i] = [int(bounds[0]), int(bounds[1])]

ranges.sort()
intersect = [ranges[0]]

# Merge intersecting intervals
for i in range(1, len(ranges)):
    last = intersect[-1]
    curr = ranges[i]
    if curr[0] <= last[1]:
        last[1] = max(last[1], curr[1])
    else:
        intersect.append(curr)

res = int()
for item in intersect:
    res += (item[1] - item[0]) + 1

print(res)
