a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == 0 and b == 0:
    print("INF")
elif a == 0:
    print("NO")
elif c == 0:
    print((- b) // a)
elif (b / a) == (d / c):
    print("NO")
elif -b % a == 0:
    print((-b) // a)
else:
    print("NO")
