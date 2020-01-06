import math

# TODO: make this more efficient

answer = 0

for x in range(1, 1_000_000+1):
    nr = x
    terms = []
    while True:
        terms.append(nr)
        nr = sum([math.factorial(int(d)) for d in str(nr)])
        if nr in terms:
            if len(terms) == 60:
                answer += 1
            break

print('answer:', answer)