n = int(input())
i = 1
if n >= i:
    while n >= i:
        i = i * 2
        if n // i == 1 and n % i == 0 and i != 1:
            print('YES')
            break
        elif n == 1:
            print("YES")
        elif n < i:
            print("NO")
