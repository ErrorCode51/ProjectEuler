answer = 1
e = 0

iteration = 1
index = 0
while True:
    endingIndex = index + len(str(iteration))
    if index < (10**e) and endingIndex >= (10**e):
        digit = int(str(iteration)[(10**e)-index-1])
        answer *= digit
        print(str(10**e) + ':', digit)
        if e == 6:
            break
        e += 1

    index = endingIndex
    iteration += 1

print('product:', answer)