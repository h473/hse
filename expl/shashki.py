a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if b2 % 2 == 0:
    if a2 % 2 == 0 and b2 > b1:
        print("YES")
    else:
        print("NO")
elif b2 % 2 != 0:
    if a2 % 2 != 0 and b2 > b1:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
