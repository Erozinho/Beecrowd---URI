while True:
    try:
        N1,N2 = map(int,input().split())
        print (N1 ^ N2)
    except EOFError:
        break
