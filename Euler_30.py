# quick and dirty calculate the maximum number to check
i = 1
while True:
    if int('9'*i) > i * (9**5):
        break
    else:
        i +=1

limit = int('9'*i) +1
print('limit:', limit)

# check all numbers
total = 0
for x in range(2, limit):
    if x == sum([int(y)**5 for y in str(x)]):
        total += x

print('total:', total)