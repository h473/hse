from math import fabs

listSize = int(input())
intList = list(map(int, input().split()))
x = int(input())
maxraznost = 2000
for i in intList:
    raznost = int(fabs(i - x))
    if raznost <= maxraznost:
        y = i
        maxraznost = raznost
print(y)
