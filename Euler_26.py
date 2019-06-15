def getMultiplier(number, divider):
    i = 1
    while True:
        if divider*i > number:
            return i -1
        i += 1

def getCycleLength(number, divider):
    answer = ''
    if divider > number:
        answer = '0.'
    remainder = number
    remainders = []
    isCyclical = False
    cycleLength = 0
    startingRemainder = None
    while True:
        if remainder >= divider:
            multiplier = getMultiplier(remainder, divider)
            answer += str(multiplier)
            if remainder not in remainders:
                remainders.append(remainder)
            else:
                if isCyclical:
                    if remainder == startingRemainder:
                        return cycleLength
                else:
                    isCyclical = True
                    startingRemainder = remainder
                cycleLength += len(str(multiplier))
            # print('remainder:', remainder, 'multiplier:', multiplier)
            remainder = remainder % (divider*multiplier)
            if remainder == 0 or len(answer) >= 10000:
                return None
        else:
            if not '.' in answer:
                answer += '.'
            remainder *= 10
            if remainder >= divider:
                continue
            answer += '0'
            if isCyclical:
                cycleLength += 1
            while remainder < divider:
                remainder *= 10



longestCycle = 0
d = 0

for i in range(1, 1000):
    print(i)
    x = getCycleLength(1, i)
    if x != None:
        if x > longestCycle:
            longestCycle = x
            d = i

print('Longest cycle =', longestCycle, 'given on d =', d)