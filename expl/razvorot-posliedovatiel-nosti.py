def Rever():
    n = int(input())
    if n != 0:
        Rever()
        print(n)
    if n == 0:
        print(0)


Rever()
