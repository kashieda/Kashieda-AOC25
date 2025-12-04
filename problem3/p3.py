with open("p3.txt") as f:
    inp = [line.rstrip() for line in f]

jolts = 0

for l in inp:
    print(l)

    max = 0

    for fn in range(len(l)-1):
        for ln in range(fn+1, len(l)):
            this = int(l[fn]+l[ln])
            if this > max:
                max = this
        
    jolts += max

print(jolts)
