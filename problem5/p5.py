with open("p5.txt") as f:
    inp = [line.rstrip() for line in f]

ranges = []
ingredient = []

r = True

for n in range(len(inp)):
    if r:
        if inp[n]!="":
            thisr = inp[n].split('-')
            ranges.append([int(thisr[0]), int(thisr[1])])
        else:
            r = False
    else:
        ingredient.append([inp[n],0])

for i in range(len(ingredient)):
    thisi = int(ingredient[i][0])

    for r in ranges:
        if r[0] <= thisi <= r[1]:
            ingredient[i][1] = 1

fresh = 0
for i in ingredient:
    if i[1]:
        fresh += 1

print(f"Found {fresh} fresh ingredients.")
        
exit()
