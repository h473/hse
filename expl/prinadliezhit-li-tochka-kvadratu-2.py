import math


def IsPointInSquare(a, b):
    return math.fabs(a) + math.fabs(b) <= 1


a = float(input())
b = float(input())
if IsPointInSquare(a, b):
    print("YES")
else:
    print("NO")
