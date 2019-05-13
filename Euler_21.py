def d(n):
    return sum([i for i in range(1, n) if n%i == 0])

amicables = []

for a in range(10000):
    b = d(a)
    if a == d(b) and a != b:
        if a not in amicables:
            amicables.append(a)

print(sum(amicables))