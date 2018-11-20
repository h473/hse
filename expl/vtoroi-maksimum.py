x = int(input())
xOld = -1
xNew = 1
while x != 0:
    if x > xNew:
        xOld = xNew
        xNew = x
    elif xOld <= x <= xNew:
        xOld = x
    x = int(input())
print(xOld)
