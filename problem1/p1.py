import re, itertools, copy

with open("p1.txt") as f:
    inp = [line.rstrip() for line in f]

position = 50
nulls = 0

for rot in inp:
    sign = 1 if rot[0]=='R' else -1

    #print(f"rotation {rot} riktning {sign}.")
    #print(f"Distans {rot[1:]}")

    dist = int(rot[1:])
    position = (position+sign*dist)%100

    if not position:
        nulls += 1

    #print(f"Ny position {position}.")


print(f"Totalt {nulls} nollor.")        
