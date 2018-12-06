n = int(input())
nList = list(map(int, input().split()))
nList.sort()


def maxshoes(n, nList):
    j = 0
    for i in nList:
        if i >= n:
            j += 1
            n = i + 3
    return j


print(maxshoes(n, nList))
