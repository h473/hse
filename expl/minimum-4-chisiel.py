a = int(input())
b = int(input())
c = int(input())
d = int(input())


def minimal(a, b, c, d):
    result = min(min(a, b), min(c, d))
    return result


print(minimal(a, b, c, d))
