a = input().split(" ")
max = max(a)
ind = 0
for i in range(len(a)):
    i = int(i)
    if a[i] == max:
        ind = i
print(max, ind)
