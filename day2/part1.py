
def isSafe(line):
    safe = False
    increasing = False
    decreasing = False
    i=0
    safeZone=[-3, -2, -1, 1, 2, 3]
    for val in line:
        if line[i+1] == " ": break
        dif = int(line[i])-int(line[i+1])
        if dif > 0:
            if increasing:
                safe = False
                break
            decreasing = True
        elif dif < 0:
            if decreasing:
                safe = False
                break
            increasing = True
        else:
            safe = False
            break
        if dif in safeZone:
            safe = True
        i+=1
    return safe

file = open("input.txt")
safe = 0
for line in file:
    values = [x.strip() for x in line.split(' ')]
    print(values)
    if isSafe(line):
        safe +=1
file.close()
print(safe)
