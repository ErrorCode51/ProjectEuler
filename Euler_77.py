# https://stackoverflow.com/questions/14218882/a-number-as-its-prime-number-parts
import math

def isPrime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)+1), 2):
        if number % i == 0:
            return False
    return True

i = 0
j = 2
primes = []

def genNewPrime():
    global primes
    global i
    while True:
        i += 1
        if isPrime(i):
            primes.append(i)
            return


def recursiveMess(goal, startNr=0, minimal=0):
    global primes
    answer = 0
    for p in primes:
        if p < minimal:
            continue
        if startNr+p > goal:
            return answer
        if startNr+p == goal:
            return answer+1
        answer += recursiveMess(goal, startNr+p, p)
    return answer

while len(primes) < 50:
    genNewPrime()

while True:
    while j < i:
        primePartitions = recursiveMess(j)
        if primePartitions > 5000:
            break
        j +=1
    if j < i: # if inner loop was broken
        break
    genNewPrime()

print('answer:', j)