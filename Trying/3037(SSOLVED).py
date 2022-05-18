def arremessos():
    pontos = 0
    for A in range(3):
        jogada = input().split()
        D = int(jogada[0])
        Y = int(jogada[1])
        pontos += D * Y
    return pontos

N = int(input())
for X in range(N):
    PJ = arremessos()
    PM = arremessos()
    if int(PJ) > int(PM):
        print("JOAO")
    else:
        print("MARIA")
