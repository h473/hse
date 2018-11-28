n = int(input())
sum = 0
k = 1
for i in range(1, n + 1):
    k = k * i
    sum += k
print(sum)
