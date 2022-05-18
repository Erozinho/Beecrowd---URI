s,j = 0,0
while j != 1:
    N,M = map(int,input().split())
    s = 0
    if N > M:
        NUM = N
        N = M
        M = NUM
    if N <= 0 or N <= 0:
        j = 1
    if j != 1:
        for x in range(N, M + 1):
            s += x
            print("{} ".format(x),end="")
            if x == M:
                print("Sum={}".format(s))
