a = list((map(int, input().split())))
b = list((map(int, input().split())))


def merge(a, b):
    i, j = 0, 0
    c = []
    while i <= len(a) and j <= len(b):
        if i == len(a):
            if j == len(b):
                return c
            else:
                c.append(b[j])
                j += 1
        elif j == len(b):
            c.append(a[i])
            i += 1
        elif a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    return c


print(*merge(a, b))
