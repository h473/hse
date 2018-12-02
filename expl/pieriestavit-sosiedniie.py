intList = list(map(int, input().split()))
newList = list()
if len(intList) % 2 == 0:
    for i in range(len(intList)):
        if i == 0 or i % 2 == 0:
            newList.append(intList[i + 1])
            newList.append(intList[i])
else:
    for i in range(len(intList) - 1):
        if i == 0 or i % 2 == 0:
            newList.append(intList[i + 1])
            newList.append(intList[i])
    newList.append((intList[len(intList) - 1]))
print(*newList)
