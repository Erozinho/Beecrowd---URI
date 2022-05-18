while True:
    try:
        N1,N2 = map(int,input().split())
        N3 = 0
        for x in range(N1, N2+1):
            if len(set(list(str(x)))) == len(str(x)):
                N3 += 1
                print(N3)
        
    except EOFError:
        break
