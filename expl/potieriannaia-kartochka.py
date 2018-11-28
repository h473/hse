n = int(input())
sumall = 1
sum = 0
for i in range(2, n + 1):
    sumall += i
    m = int(input())
    sum += m
print(sumall - sum)
