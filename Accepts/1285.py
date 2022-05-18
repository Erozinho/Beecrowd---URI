while True:
    try:
        N, M = map(int,input().split())
        NUM = 0
        for X in range(N, M + 1):
            if len(set(list(str(X)))) == len(str(X)):
                NUM += 1
        print(NUM)
    except EOFError:
        break
