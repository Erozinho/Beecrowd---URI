while True:
    N = int(input())
    if N > 0:
        for x in range(1, N + 1):
            if x == N:
                print("{}".format(x),end="\n")
            else:
                print("{}".format(x),end=" ")
            J = 0
    else:
        break
