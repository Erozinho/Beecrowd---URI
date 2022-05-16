N = int(input())
for Y in range(N):
    X = int(input())
    if (X % X == 0) and (X % 2 != 0) and (X % 3 != 0):
        print("{} eh primo".format(X))
    else:
        print("{} nao eh primo".format(X))
