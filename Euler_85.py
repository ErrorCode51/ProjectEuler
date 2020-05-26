def nrOfRectanglesInGrid(gridWidth, gridHeight):
    total = 0
    for x in range(1, gridWidth+1):
        for y in range(1, gridHeight+1):
            total += ((gridWidth-x)+1)*((gridHeight-y)+1)
    return total

#

closestValue = (0, 0)
width = 1
height = 1

while True:
    rects = nrOfRectanglesInGrid(width, height)
    if abs(2_000_000-rects) < abs(2_000_000-closestValue[0]):
        closestValue = (rects, width*height)
    if rects > 2_000_000:
        if width == 1:
            break
        width = 1
        height += 1
        continue
    width += 1

print(closestValue[1])