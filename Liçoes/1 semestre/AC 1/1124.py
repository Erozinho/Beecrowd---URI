A = int(input())
if A%2 and A >=2:
    print("{} {}".format(A - 2, A + 1))
elif (A%2) == 0 and A >= 2:
    print("{} {}".format(A - 1, A + 2))
