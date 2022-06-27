while True:
    try:
        N,M = map(int,input().split())
        T,T1,F,F1 = 1,1,1,1
        while T1 <= N:
            F = F * T1
            T1 = T1 + 1
        while T <= M:
            F1 = F1 * T
            T = T + 1
        print("{}".format(F+F1))
    except EOFError:break
