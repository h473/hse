n = int(input())
if n == 0 or 10 <= n <= 20 or 5 <= (n % 10) <= 9 or n % 10 == 0:
    print(n, "korov")
elif n % 10 == 1:
    print(n, "korova")
else:
    print(n, "korovy")
