def flip(arr):

    ly = len(arr)

    lx = 0
    for l in arr:
        if lx < len(l):
            lx = len(l)
            
    
    #lx = len(arr[0])

    #print(f"{lx=}, {ly=}")
    
    res = []
    for x in range(lx):
        line = ''
        for m in range(ly):
            if (lx-x)>len(arr[m]):
                line+=' '
            else:
                line += arr[m][lx-x-1]
        res.append(line)

    return res

with open("p6.txt") as f:
    inp = [line.rstrip() for line in f]

flinp = flip(inp[0:-1])

op = []

for ops in inp[-1].split(None):
    op.append(ops)
    
summa = 0

for calc in range(len(op)):
    thisop = op[calc]

    if thisop == '+':
        start = 0
    else:
        start = 1
        
    fac = True
    more = True

    print(f"Calc number: {calc}")
    
    while fac:
        if len(flinp) == 0:
            thisfactor = "    "
            more = False
        else:
            thisfactor = flinp[-1]

        if thisfactor == "    ":
            summa += start
            fac = False
        elif thisop == '+':
            #print(f"{start } + {thisfactor} =", end = " ")
            start += int(thisfactor)
            #print(f"{start}")
        else:
            #print(f"{start } * {thisfactor} =", end = " ")
            start *= int(thisfactor)
            #print(f"{start}")

        if more:
            flinp.pop()

print(f"Sum of all calculations: {summa}")
quit()
    
