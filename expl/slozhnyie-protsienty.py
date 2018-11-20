p = int(input())
x = int(input())
y = int(input())
k = int(input())
n = 2
px = int((x * 100 + y) * (100 + p) / 100)
while n <= k:
    x = int(px // 100)
    y = int(round(((px / 100) % 1) * 100))
    px = int((x * 100 + y) * (100 + p) / 100)
    n += 1
print((px // 100), round(((px / 100) % 1) * 100))
