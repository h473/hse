def Rev():
    n = int(input())
    if n != 0:
        Rev()
        print(n)
    if n == 0:
        print(0)


Rev()
