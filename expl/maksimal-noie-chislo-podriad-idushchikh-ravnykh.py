x = int(input())
xlast = -1
k = 1
k2 = 1
while x != 0:
    if x == xlast:
        k += 1
    else:
        xlast = x
        k2 = max(k, k2)
        k = 1
    x = int(input())
print(max(k, k2))
