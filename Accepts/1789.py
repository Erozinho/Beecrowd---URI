while True:
    try:
        N_LESMA = int(input())
        VELOCIDADE = list(map(int,input().split()))
        if len(VELOCIDADE) == N_LESMA:
            if max(VELOCIDADE) < 10:
                print(1)
            elif max(VELOCIDADE) >= 10 and max(VELOCIDADE) < 20:
                print(2)
            else:
                print(3)
        else:
            break
    except EOFError:
        break
