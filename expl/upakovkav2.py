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
        if max(l1, l2) <= lc and max(w1, w2) <= wc:
            print("YES")
        elif max(w1, l2) <= lc and max(w2, l1) <= wc:
            print("YES")
        elif max(l1, w2) <= lc and max(w1, l2) <= wc:
            print("YES")
        elif max(w1, w2) <= lc and max(l1, l2) <= wc:
            print("YES")
        else:
            print("NO")
    elif w1 + w2 <= wc and max(h1, h2) <= hc:
        if max(l1, l2) <= lc:
            print("YES")
        else:
            print("NO")
    elif l1 + l2 <= wc and max(h1, h2) <= hc:
        if max(w1, w2) <= lc:
            print("YES")
        else:
            print("NO")
    elif w1 + l2 <= wc and max(h1, h2) <= hc:
        if max(l1, w2) <= lc:
            print("YES")
        else:
            print("NO")
    elif l1 + w2 <= wc and max(h1, h2) <= hc:
        if max(l2, w1) <= lc:
            print("YES")
        else:
            print("NO")
    elif l1 + l2 <= lc and max(h1, h2) <= hc:
        if max(w1, w2) <= wc:
            print("YES")
        else:
            print("NO")
    elif l1 + w2 <= lc and max(h1, h2) <= hc:
        if max(w1, l2) <= wc:
            print("YES")
        else:
            print("NO")
    elif w1 + l2 <= lc and max(h1, h2) <= hc:
        if max(l1, w2) <= wc:
            print("YES")
        else:
            print("NO")
    elif w1 + w2 <= lc and max(h1, h2) <= hc:
        if max(l1, l2) <= wc:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")
