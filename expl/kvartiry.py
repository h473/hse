x = int(input())
y = int(input())
c = int(y % (y - x + 1))
if 1 <= x <= y and c == 0:
        print("YES")
else:
    print("NO")
