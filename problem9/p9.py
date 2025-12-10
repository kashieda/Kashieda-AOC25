def dist(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2 

coords = []

with open("p9.txt") as f:
    inp = [line.rstrip() for line in f]

for l in inp:
    cl = l.split(',')
    coords.append([int(cl[0]), int(cl[1])])

maxarea = 0

for c1 in range(len(coords)):
    for c2 in range(c1+1, len(coords)):
        thisarea = ((abs(coords[c1][0]-coords[c2][0])+1)*
                     (abs(coords[c1][1]-coords[c2][1])+1))

        #print(f"{coords[c1]=}, {coords[c2]=} and {thisarea=}")
        
        if thisarea > maxarea:
            maxarea = thisarea

print(f"The maximum possible area is {maxarea}")
        
        


    
