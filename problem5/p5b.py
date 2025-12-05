def merge_range(intervals):
    
    intervals.sort()

    res = []
    res.append(intervals[0])

    for i in range(1, len(intervals)):
        last = res[-1]
        curr = intervals[i]

        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            res.append(curr)

    return res

with open("p5.txt") as f:
    inp = [line.rstrip() for line in f]

ranges = []

r = True

for n in range(len(inp)):
    if r:
        if inp[n]!="":
            thisr = inp[n].split('-')
            ranges.append([int(thisr[0]), int(thisr[1])])
        else:
            r = False

merged = merge_range(ranges)

fresh = 0

for r in merged:
    fresh += r[1]-r[0]+1

print(f"Found {fresh} potentially fresh ingredients.")
