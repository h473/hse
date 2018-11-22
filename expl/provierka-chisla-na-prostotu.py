n = int(input())


def IsPrime(n):
    i = 2
    d = 0
    while i <= n ** 0.5 and i > 1:
        if n % i == 0:
            d += 1
        i += 1
    return d == 0


if IsPrime(n):
    print("YES")
else:
    print("NO")
