while True:
    try:
        N = int(input())
        if 1001 <= N <= 9999:
            print(N-1)
        else:
            break
    except EOFError:
        break
