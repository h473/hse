s = input()
first = s.find('f')
last = s.rfind('f')
if last == -1:
    print()
elif first == last:
    print(first)
else:
    print(first, last)
