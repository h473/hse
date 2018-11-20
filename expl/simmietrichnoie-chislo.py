n = int(input())
right = int((n // 1000 % 10) * 10 + (n // 100 % 10))
left = int((n % 10 * 10) + (n // 10 % 10))
print(1 + (right - left))
