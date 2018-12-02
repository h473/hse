intList = list(map(int, input().split()))
maxind = 0
minind = 0
for i in range(len(intList)):
    if intList[i] > intList[maxind]:
        maxind = i
    elif intList[i] < intList[minind]:
        minind = i
intList[minind], intList[maxind] = intList[maxind], intList[minind]
print(*intList)
