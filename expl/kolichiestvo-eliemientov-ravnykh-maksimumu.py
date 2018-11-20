x = int(input())
xmax = x
k = 0
while x != 0:
    if x > xmax:
        xmax = x
        k = 1
    elif x == xmax:
        k += 1
    x = int(input())
print(k)
