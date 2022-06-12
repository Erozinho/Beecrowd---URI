while True:
    try:
        NOTAS = []
        N,Q = map(int,input().split())
        for x in range(N):NOTAS.append(int(input()))
        NOTAS.sort()
        NOTAS.reverse()
        for i in range(Q):
            CONSULTA = int(input())
            print("{}".format(NOTAS[CONSULTA-1]))
    except EOFError:
        break
