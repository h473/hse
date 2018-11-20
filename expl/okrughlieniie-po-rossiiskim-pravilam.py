import math
x = float(input())
x2 = math.floor(x)
x3 = ((x - x2) * 10)
if x3 >= 5:
    x = math.ceil(x)
else:
    x = math.floor(x)
print(x)
