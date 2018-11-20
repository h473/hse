k = int(input())
m = int(input())
n = int(input())
if n <= k:
    x = 2*m
elif n*2 % k == 0:
    x = m * (n * 2 // k)
else:
    x = m * (1 + (n * 2 // k))
print(x)
