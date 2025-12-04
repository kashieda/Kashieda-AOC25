with open("p4.txt") as f:
    inp = [line.rstrip() for line in f]

numline = len(inp)
numpos = len(inp[0])

print(f"{numline=}, {numpos=}")

for l in inp:
    print(l)

numrolls = 0

removed = True

while removed:
    removed = False
    positions = []
    
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
                            
                if string.count('@')<4:
                    numrolls += 1
                    removed = True
                    positions.append([line, pos])
        
    for pos in positions:
        l = pos[0]
        p = pos[1]

        new = inp[l][0:p]+"."+inp[l][(p+1):numpos]

        inp[l] = new
        
print(f"{numrolls=}")
                        
