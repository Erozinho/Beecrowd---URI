N_CASOS = int(input())
for i in range(N_CASOS):
    soma,CONTROLE = 0,1
    X,Y = map(int,input().split())
    while CONTROLE <= Y:
        if X % 2 != 0:
            soma += X
            X += 1
            CONTROLE += 1
        else:
            X += 1
    print("{}".format(soma))
