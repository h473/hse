n = int(input())
sum = 0
k = 1
while k <= n:
    sum += (1 / n ** 2)
    n = n - 1
print(sum)
