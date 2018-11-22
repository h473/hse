def IsPointInSquare(a, b):
    return a <= 1 and a >= -1 and b <= 1 and b >= -1


a = float(input())
b = float(input())
if IsPointInSquare(a, b):
    print("YES")
else:
    print("NO")
