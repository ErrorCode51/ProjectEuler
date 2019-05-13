import math
a = 999
b = 999

def isPalindrome(number):
    number = str(number)
    for i in range(math.floor(len(number)/2)):
        ii = ((i * -1) -1)
        if (number[i] != number[ii]):
            return 0
    return 1

largest = 0

while (1):
    ab = (a * b)
    if (isPalindrome(ab)):
        if (ab > largest):
            largest = ab
    a -= 1
    if (a == 99):
        a = 999
        b -= 1
        if (b == 99):
            break

print("Largest palindrome: " + str(largest))
