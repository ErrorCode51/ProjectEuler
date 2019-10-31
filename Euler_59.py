from itertools import product
import string
chars = []

with open('ProblemFiles/Problem_59.txt') as f:
    for line in f:
        chars = [int(x) for x in line.split(',')]

# a list to keep track of what key produces the most letters, as this is probably the right key
mostLetters = [0]

for key in product(range(97, 123), repeat=3):
    nrOfLetters = 0
    keyPosition = 0
    decrypted = ''
    for c in chars:
        char = c^key[keyPosition]
        if chr(char) in string.ascii_letters:
            nrOfLetters += 1
        keyPosition += 1
        if keyPosition == 3:
            keyPosition = 0
        decrypted += chr(char)
    if nrOfLetters > mostLetters[0]:
        mostLetters = [nrOfLetters, key, decrypted]

print('key:', ''.join([chr(c) for c in mostLetters[1]]))
print('password:', mostLetters[2])
print('answer to problem:', sum([ord(c) for c in list(mostLetters[2])]))
