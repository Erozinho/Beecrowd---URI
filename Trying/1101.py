I = 0
while I != 1:
    # TODO: write code...
    M, N = map(int,input().split())
    if M == 0 or N == 0:
        print("")
    elif M > N:
        print("{} {} {} {} Sum={}".format(N, (N + 1), (M - 1), M, (N + (N + 1) + (M - 1) + M)))
    elif M < N:
        print("{} {} {} {} Sum={}".format(M, (M + 1), (M - 1), N, (N + (M + 1) + (N - 1) + M)))
