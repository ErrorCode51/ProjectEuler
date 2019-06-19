number = 0

# quick and dirty
for i in range(1000):
    j = i + 1
    number += j**j
print('answer:', str(number)[-10:])