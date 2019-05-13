print("Hello World")

from includeFiles.Functions import *

number = 0
total = 0

while(number < 1000):
    if check3(number) or check5(number):
        print(number)
        total += number
    number += 1

print("Total:" + str(total))
