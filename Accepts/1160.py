N_CASOS = int(input())
for i in range(N_CASOS):
    PA,PB,G1,G2 = map(float,input().split())
    PA,PB,ANO = int(PA),int(PB),0
    while PA <= PB:
        PA = int(PA * (1 + G1 / 100))
        PB = int(PB * (1 + G2 / 100))
        ANO += 1
        if ANO > 100:
            break
    if ANO > 100:
        print("Mais de 1 seculo.")
    else:
        print("{} anos.".format(ANO))
