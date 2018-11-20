a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
hole = d * e
brick1 = a * c
brick2 = a * b
brick3 = b * c
if (d >= a and e >= c) or (d >= c and e >= a):
    if hole >= brick1:
        print("YES")
elif (d >= a and e >= b) or (d >= b and e >= a):
    if hole >= brick2:
        print("YES")
elif (d >= b and e >= c) or (d >= c and e >= b):
    if hole >= brick3:
        print("YES")
else:
    print("NO")
