highest = 0

for i in range(2, 100000):
    string = ''
    for x in range(9):
        string += str(i*(x+1))
        if len(string) >= 9:
            break
    if ''.join(sorted(string)) == '123456789':
        if int(string) > highest:
            highest = int(string)

print('highest:', highest)
