J = 0
while J != 1:
    N = int(input())
    if N > 0:
        for x in range(1, N + 1):
            print("{} ".format(x),end="")
            J = 0
    else:
        J = 1
