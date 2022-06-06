N_BOLAS = int(input())
BOLAS = list(map(int,input().split()))
if len(BOLAS) == N_BOLAS:
    while len(BOLAS) != 1:
        bola = []
        for x in range(len(BOLAS) - 1):
            if BOLAS[x] == BOLAS[x+1]: bola.append(1)
            else: bola.append(-1)
        BOLAS = bola[:]
    if bola[0] == 1: print("preta")
    else: print("branca")
