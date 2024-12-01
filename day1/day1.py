def findSum(list1, list2):
    i = 0
    count = 0
    print(len(list1))
    while i < len(list1):
        value = abs(int(list1[i]) - int(list2[i]))
        count += value
        i += 1
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
print(col1)
col2.sort()
total = findSum(col1, col2)
print(total)
