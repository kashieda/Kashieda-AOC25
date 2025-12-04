with open("p3.txt") as f:
    inp = [line.rstrip() for line in f]

jolts = 0

for l in inp:
    print(l)

    max = 0

    ln = len(l)
    
    for n1 in range(ln-11):
        print(f"Starting with digit {n1}")
        for n2 in range(n1+1, ln-10):
            for n3 in range(n2+1, ln-9):
                for n4 in range(n3+1, ln-8):
                    for n5 in range(n4, ln-7):
                        for n6 in range(n5+1, ln-6):
                            for n7 in range(n6+1, ln-5):
                                for n8 in range(n7+1, ln-4):
                                    for n9 in range(n8+1, ln-3):
                                        for n10 in range(n9+1, ln-2):
                                            for n11 in range(n10+1, ln-1):
                                                for n12 in range(n11+1, ln):
                                                    
                                                    this = int(l[n1]+l[n2]+l[n3]+l[n4]+l[n5]+l[n6]
                                                               +l[n7]+l[n8]+l[n9]+l[n10]+l[n11]+l[n12])
                                                    if this > max:
                                                        max = this
        
    jolts += max

print(jolts)
