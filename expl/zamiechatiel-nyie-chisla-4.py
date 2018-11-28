a = int(input())
b = int(input())
for i in range(a, b + 1):
    l = tuple(str(i))
    if int(l[0]) == int(l[3]) and int(l[1]) == int(l[2]):
        print(i)
