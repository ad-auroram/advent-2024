def findVals(list1, list2):
    count = 0
    # go through list 1
    for val in list1:
        valCount = 0
        for item in list2:
            if val == item:
                valCount += 1
                list2.remove(item)
                print(len(list2))
        count += valCount * (int(val))
    return count


col1 = []
col2 = []
file = open("input.txt")
for line in file:
    values = line.split("   ")
    col1.append(values[0].strip())
    col2.append(values[1].strip())
file.close()
col1.sort()
col2.sort()
answer = findVals(col1, col2)
print(answer)
