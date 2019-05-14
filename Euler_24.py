numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

permutationIndex = 0

def getPermuatations(numbers, n):
    if len(numbers) <= 1:
        global permutationIndex
        permutationIndex += 1
        if permutationIndex == 1000000:
            print((n*10) + numbers[0])
    else:
        for num in numbers:
            numbers.remove(num)
            getPermuatations(numbers, (n*10)+num)
            numbers.append(num)
            numbers.sort()

getPermuatations(numbers, 0)
