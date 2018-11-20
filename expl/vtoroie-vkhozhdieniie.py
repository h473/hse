s = input()
pos = 0
n = 1
if s.find('f', pos) != -1:
    while s.find('f', pos) != -1:
        pos = s.find('f', pos) + 1
        n += 1
        if n == 2:
            print(s.find('f', pos))
elif s.find('f', pos) == -1:
    print(-2)
