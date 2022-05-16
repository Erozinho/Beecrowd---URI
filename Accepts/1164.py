VEZES = int(input())
for X in range(VEZES):
    S = 0
    N_VERIFI = int(input())
    for M in range(1,N_VERIFI):
        if (N_VERIFI % M == 0):
            S += M
    if S == N_VERIFI:
        print("{} eh perfeito".format(N_VERIFI))
    else:
        print("{} nao eh perfeito".format(N_VERIFI))
