a = input().split()
k = 0
for i in a:
    i = int(i)
    if i % 2 == 0:
        k += 1
print(k)
