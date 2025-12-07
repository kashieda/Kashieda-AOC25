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

with open("p7.txt") as f:
    inp = [line.rstrip() for line in f]


radl = len(inp[0])
    
for p in range(radl):
    if inp[0][p] == 'S':
        start = p

res = [inp[0]]

splits = 0

for l in range(1, len(inp)):
    thisline = ''

    for p in range(radl):
        hasbeam = False

        # 'S' = start
        # '|' = has beam
        # 'P' = non-active splitter
        # 'A' = active splitter

        above = res[l-1][p]
        upleft = '' if p==0 else res[l-1][p-1]
        upright = '' if p==(radl-1) else res[l-1][p+1]
        this = inp[l][p]
        
        upside = upleft + upright
        
        if above in ['S', '|']:
            hasbeam = True
            #print("There is a beam!")
        elif 'A' in upside:
            hasbeam = True

        add = '.'
            
        if this == '^':
            add = 'A' if hasbeam else 'P'
            splits += 1 if hasbeam else 0
        elif hasbeam:
            add = '|'
            
        thisline += add

    print(thisline)
    res.append(thisline)

print(f"Total {splits=}.")
