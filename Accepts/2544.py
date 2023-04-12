while True:
    try:
        N = int(input())
        if N == 1:
            print(0)
        else:
            i = 0
            while i < N:
                resultado = pow(2, i)
                if (resultado == N):
                    print(i)
                    break
                i += 1
    except EOFError:
        break
