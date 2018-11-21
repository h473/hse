x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())


def p(x1, y1, x2, y2, x3, y3):
    ab = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    ac = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
    bc = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
    p = ab + bc + ac
    return p


print(p(x1, y1, x2, y2, x3, y3))
