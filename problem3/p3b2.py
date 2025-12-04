import re

def fbd(numstr):
    #print(numstr)

    for d in range(9, 0, -1):
        # hitta första d i numstr
        # om hittad, returnera position och värde
        #print(d)

        if (pos := numstr.find(str(d))) != -1:
            #print(d)
            return d, pos


with open("p3.txt") as f:
    inp = [line.rstrip() for line in f]

        # bästa är 0? 
    
jolts = 0

for l in inp:
    #print(l)

    best = ''

    ln = len(l)

    # hitta bästa nuffran bland de max (längd - 12 + pos) sista
    # spara positionen och värdet; fortsätt tills alla 12 siffrorna är klara
    
        
    start = 0
    
    for i in range(12):
        result = fbd(l[start:(ln-11+i)])
        
        start += result[1]+1
        best += str(result[0])

    jolts += int(best)

    print(f"        {int(best)}")
print(f"\n {jolts=}")
