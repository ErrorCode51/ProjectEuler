total = 1 #already taking into account the two pound coin

for a in range(3): # pound coins, max 2
    for b in range(5): # 50 pence coins, max 4
        for c in range(11): # 20 pence coins, max 10
            for d in range(21): # 10 pence coins, max 20
                for e in range(41): # 5 pence coins, max 40
                    for f in range(101): # 2 pence coins, max 100
                        if (a*100) + (b*50) + (c*20) + (d*10) + (e*5) + (f*2) <= 200:
                            total += 1
                        else:
                            break

print(total)