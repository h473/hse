def sum(a, b):
    n = min(a, b)
    m = max(a, b)
    if a == b:
        a = a * 2
        return a
    else:
        while n > 0:
            m = m + 1
            n = n - 1
        return m


a = int(input())
b = int(input())
print(sum(a, b))
