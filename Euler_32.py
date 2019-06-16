products = []

for x in range(2000):
    for y in range(500):
        if ''.join(sorted(str(x) + str(y) + str(x*y))) == '123456789':
            print(x, '*', y, '=', x*y)
            if x*y not in products:
                products.append(x*y)

print('total:', sum(products))