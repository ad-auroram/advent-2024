
def isSafe(line):
    isSafe = True
    increasing = False
    decreasing = False
    i = 0
    safeZone = [-3, -2, -1, 1, 2, 3]
    while i<len(line)-1:
        dif = int(line[i])-int(line[i+1])
        if dif > 0:
            if increasing:
                isSafe = False
                break
            decreasing = True
        elif dif < 0:
            if decreasing:
                isSafe = False
                break
            increasing = True
        else:
            isSafe = False
            break
        if dif not in safeZone:
            isSafe = False
            break
        i+=1
    return isSafe

file = open("input.txt")
safe = 0
for line in file:
    values = [x.strip() for x in line.split(' ')]
    if isSafe(values):
        safe +=1
file.close()
print(safe)
