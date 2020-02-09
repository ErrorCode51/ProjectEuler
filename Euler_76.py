# https://en.wikipedia.org/wiki/Partition_function_(number_theory)#Recurrence_relations

partitionCache = [None] * 101


def getPentagonalNumber(k):
    return (k*((3*k) -1))//2


def pentagonGenerator():
    k = 0
    while True:
        k += 1
        yield k, getPentagonalNumber(k)
        yield -k, getPentagonalNumber(-k)


def P(n):
    global partitionCache
    if n < 0:
        return 0
    if n <= 1:
        return 1
    if partitionCache[n]:
        return partitionCache[n]
    answer = 0
    for p in pentagonGenerator():
        if n-p[1] < 0:
            partitionCache[n] = answer
            return answer
        answer += int((-1)**(p[0]+1)) * P(n - p[1])


print('answer:', P(100)-1)
