def ReduceFraction(n, m):
    x = 2
    v = 1
    while x <= n and x <= m:
        if n % x == 0 and m % x == 0:
            v = x
        x += 1
    return (n // v, m // v)


n = int(input())
m = int(input())
p, q = ReduceFraction(n, m)
print(p, q)
