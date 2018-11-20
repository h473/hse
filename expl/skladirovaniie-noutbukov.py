a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
m1 = (a1 // a2) * (b1 // b2) * (c1 // c2)
m2 = (a1 // a2) * (b1 // c2) * (c1 // b2)
m3 = (a1 // b2) * (b1 // a2) * (c1 // c2)
m4 = (a1 // b2) * (b1 // c2) * (c1 // a2)
m5 = (a1 // c2) * (b1 // a2) * (c1 // b2)
m6 = (a1 // c2) * (b1 // b2) * (c1 // a2)
if a1 > b1:
    (a1, b1) = (b1, a1)
if b1 > c1:
    (b1, c1) = (c1, b1)
if a1 > b1:
    (a1, b1) = (b1, a1)
if a2 > b2:
    (a2, b2) = (b2, a2)
if b2 > c2:
    (b2, c2) = (c2, b2)
if a2 > b2:
    (a2, b2) = (b2, a2)
if a1 >= a2 and b1 >= b2 and c1 >= c2:
    if m1 > m2 and m1 > m3 and m1 > m4 and m1 > m5 and m1 > m6:
        print(m1)
    elif m2 > m3 and m2 > m4 and m2 > m5 and m2 > m6:
        print(m2)
    elif m3 > m4 and m3 > m5 and m3 > m6:
        print(m3)
    elif m4 > m5 and m4 > m6:
        print(m4)
    elif m5 > m6:
        print(m5)
    else:
        print(m6)
else:
    print(0)
