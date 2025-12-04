with open("p4.txt") as f:
    inp = [line.rstrip() for line in f]

numline = len(inp)
numpos = len(inp[0])

print(f"{numline=}, {numpos=}")

for l in inp:
    print(l)

numrolls = 0

for line in range(numline):
    for pos in range(numpos):
        if inp[line][pos] =="@":
            pf = max(0, pos-1)
            pl = min(pos+1, numpos-1)
            lf = max(0, line-1)
            ll = min(line+1, numline-1)
                
            string = ''
                
            for l in range(lf, ll+1):
                for p in range(pf, pl+1):
                    if p==pos and l==line:
                        string += 'x'
                    else:
                        string += inp[l][p]
                            
            print(f"{string=}, {string.count('@')}")
                            
            if string.count('@')<4:
                numrolls += 1
        
print(f"{numrolls=}")
                        
