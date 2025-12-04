with open("p2.txt") as f:
    inp = [line.rstrip() for line in f]

ranges = inp[0].split(",")

summa = 0

for r in ranges:
    start = int(r.split("-")[0])
    stop = int(r.split("-")[1])

    print(start, stop)

    for n in range(start, stop+1):
        ns = str(n)
        l = len(ns)

        unfound = True
        
        #print(l)
        #print(ns)
        for div in range(1, int(l/2)+1):
            #print(div)
            if unfound:
                if not l%div:
                    ##print(f"{ns}, {l=}")
                    s1 = ns[0:div]
                    rep = int(l/div)
                
                    cs = rep*s1
                    #print(f"{cs=} = {rep=} * {s1}")
                
                    if ns == cs:
                        #print(f"Träff: {ns}, {cs}")
                        summa += n
                        unfound = False

print(f"Summan är {summa}")
