l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())
if l2 - r1 < 1 and l3 - r2 < 1:
    print(0)
elif l2 - r1 < 1 and l3 - r2 > 0:
    print(3)
elif l2-r1 > 0 and l3 - r2 < 1:
    print(1)
else:
    print(-1)
