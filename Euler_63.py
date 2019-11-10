answer = 0
i=1

while True:
    if len(str(9**i)) < i: # stop condition
        break
    for y in range(1, 10): # 10 to the power of something, always has more digits than that something specifies
        if len(str(y**i)) == i:
            answer +=1
        y+=1
    i+=1

print('answer:', answer)