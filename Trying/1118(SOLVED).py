T,M,C = 0,0,True
while C == True:
    NOTA = float(input())
    if NOTA >= 0 and NOTA <= 10:
        M += NOTA
        T += 1
        if T == 2:
            print("media = {}".format(M/ 2))
            T = 0
            M = 0
            while True:
                A = int(input("novo calculo (1-sim 2-nao)\n"))
                if A == 1:
                    C = True
                    break
                if A == 2:
                    C = False
                    break
    else:
        print("nota invalida")
