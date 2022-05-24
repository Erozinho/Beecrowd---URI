while True:
    X = int(input())
    CONTROLE,soma = 1,0
    if X == 0:
        break
    else:
        while CONTROLE <= 5:
            if X % 2 == 0:
                soma += X
                X += 1
                CONTROLE += 1
            else:
                X += 1
    print("{}".format(soma))
