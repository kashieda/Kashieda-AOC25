with open("p1.txt") as f:
    inp = [line.rstrip() for line in f]

position = 50

nulls = 0

for rot in inp:
    clicks = 0
    sign = 1 if rot[0]=='R' else -1
    dist = int(rot[1:])
    nypos = position + sign*dist
    
    if nypos > 100:
        clicks = nypos//100
        print(f"Från {position} till {nypos} är det {clicks} klick.")
        nulls += clicks
    elif nypos < 0:
        clicks = nypos//(sign*100) +1
        if not position: # don't count ending at zero twice - adding below
            clicks -= 1
        print(f"Från {position} till {nypos} är det {clicks} klick.")
        nulls += clicks

    position = (position+sign*dist)%100

    if not position:
        if not clicks:
            print(f"Ny position {position}.")
            nulls += 1

print(f"Totalt {nulls} nollor.")        
