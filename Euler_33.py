total = 0

for x in range(10, 100):
    for y in range(x+1, 100):
        for c in (str(x)+str(y)):
            if c == '0':
                continue
            if c in str(x) and c in str(y):
                if int(str(y).replace(c, '', 1)) != 0:
                    if int(str(x).replace(c, '', 1))/int(str(y).replace(c, '', 1)) == x/y:
                        print(x, '/', y, '=', x/y)
                        if total == 0:
                            total = (x/y)
                        else:
                            total = (total * (x/y)).__round__(5) # Python has trouble working with high precision number
                        break

print('total:', total)
print('lowest denominator:', 1/total)