l1 = int(input())
w1 = int(input())
h1 = int(input())
l2 = int(input())
w2 = int(input())
h2 = int(input())
lc = int(input())
wc = int(input())
hc = int(input())
if lc >= l1 and lc >= l2 and wc >= w1 and wc >= w2 and hc >= h1 and hc >= h2:
    if h1 + h2 <= hc:
        if lc >= l1 and lc >= l2:
            print("YES")
        elif lc >= w1 and lc >= w2:
            print("YES")
        elif wc >= l1 and wc >= l2:
            print("YES")
        elif wc >= w1 and wc >= w2:
            print("YES")
        else:
            print("NO")
    elif w1 + w2 <= wc:
        if hc >= h1 and hc >= h2:
            print("YES")
        else:
            print("NO")
    elif l1 + l2 <= lc:
        if hc >= h1 and hc >= h2:
            print("YES")
        else:
            print("NO")
    elif l1 + w2 <= lc:
        if l2 <= wc and w1 <= wc:
            print("YES")
        else:
            print("NO")
    elif l2 + w1 <= lc:
        if l1 <= wc and w2 <= wc:
            print("YES")
        else:
            print("NO")
    elif l2 + w1 <= wc:
        if w1 <= lc and l2 <= lc:
            print("YES")
        else:
            print("NO")
    elif l1 + w2 < wc:
        if w2 <= wc and l1 <= wc:
            print("YES")
        else:
            print("NO")
else:
    print("NO")
