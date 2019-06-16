def isPalindrome(string):
    return string == string[::-1]

total = 0

for i in range(1, 1000000):
    if isPalindrome(str(i)):
        if isPalindrome('{0:b}'.format(i)):
            total += i

print('total:', total)