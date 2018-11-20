a = int(input())
b = int(input())
c = int(input())
if (a + b) <= c or (a + c) <= b or (c + b) <= a or a + b + c <= 0:
    print("impossible")
else:
    if c > a and c > b and a ** 2 + b ** 2 - c ** 2 > 0:
        print("acute")
    if b > a and b > c and a ** 2 + c ** 2 - b ** 2 > 0:
        print("acute")
    if a > b and a > c and b ** 2 + c ** 2 - a ** 2 > 0:
        print("acute")
    if a == b == c:
        print("acute")
    if c > a and c > b and a ** 2 + b ** 2 - c ** 2 < 0:
        print("obtuse")
    if b > a and b > c and a ** 2 + c ** 2 - b ** 2 < 0:
        print("obtuse")
    if a > b and a > c and b ** 2 + c ** 2 - a ** 2 < 0:
        print("obtuse")
    if c > a and c > b and a ** 2 + b ** 2 - c ** 2 == 0:
        print("rectangular")
    if b > a and b > c and a ** 2 + c ** 2 - b ** 2 == 0:
        print("rectangular")
    if a > b and a > c and b ** 2 + c ** 2 - a ** 2 == 0:
        print("rectangular")
