with open("p6.txt") as f:
    inp = [line.rstrip() for line in f]

factors = []

for l in range(len(inp)-1):
    thisf = []
    
    for ns in inp[l].split(None):
        thisf.append(int(ns))
                
    factors.append(thisf)

op = []

for ops in inp[-1].split(None):
    op.append(ops)

summa = 0

for calc in range(len(factors[0])):
    if op[calc] == '*':
        start = 1
        for l in range(len(factors)):
            start *= factors[l][calc]
    else:
        start = 0
        for l in range(len(factors)):
            start += factors[l][calc]

    summa += start

print(f"Sum of all problems: {summa}")
