def josepheus(P, PULOS):
    PESSOAS = [i for i in range(1, P+1)]
    PULOS -= 1
    MORTO = PULOS % len(PESSOAS)
    while len(PESSOAS) > 1:
        PESSOAS.pop(MORTO)
        MORTO = (MORTO + PULOS) % len(PESSOAS)
    return PESSOAS[0]

N_TESTES = int(input())
for x in range(N_TESTES):
    P,PULOS = map(int,input().split())
    print("Case {}: {}".format(x+1, josepheus(P,PULOS)))
