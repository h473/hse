a = int(input())
b = int(input())
c = int(input())
f = int(input())


def minimal(a, b, c, f):
    result = min(min(a, b), min(c, f))
    return result


print(minimal(a, b, c, f))
