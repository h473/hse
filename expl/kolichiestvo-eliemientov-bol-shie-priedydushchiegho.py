x = int(input())
xlast = x
k = 0
while x != 0:
    if x > xlast:
        k += 1
    xlast = x
    x = int(input())
print(k)
