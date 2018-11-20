x = int(input())
xmax = x
while x != 0:
    if x > xmax:
        xmax = x
    x = int(input())
print(xmax)
