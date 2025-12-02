with open("p2.txt") as f:
    inp = [line.rstrip() for line in f]

ranges = inp[0].split(",")

summa = 0

for r in ranges:
    start = int(r.split("-")[0])
    stop = int(r.split("-")[1])

    #print(start, stop)

    for n in range(start, stop+1):
        ns = str(n)
        l = len(ns)
        
        if not l%2:
            #print(f"{ns}, {l=}")
            e1 = int(l/2)
            s2 = int(l/2)
            e2 = int(l)

            n1 = ns[0:int(l/2)]
            n2 = ns[int(l/2):l]
            
            if n1 == n2:
                #print(f"Träff: {ns}, {n1}, {n2}")
                summa += n

print(f"Summan är {summa}")
