p = int(input())
x = int(input())
y = int(input())
px = int((x * 100 + y) * (100 + p) / 100)
print((px // 100), round(((px / 100) % 1) * 100))