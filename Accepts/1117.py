T,M = 0,0
while T < 2:
    NOTA = float(input())
    if NOTA >= 0 and NOTA <= 10:
        M += NOTA
        T += 1
    else:
        print("nota invalida")
print("media = {}".format(M/ 2))
