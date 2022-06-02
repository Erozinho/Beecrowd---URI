N_T,M2,M3,M4,M5 = int(input()),0,0,0,0
SEQ = list(map(int,input().split()))
if len(SEQ) == N_T:
    for x in range(N_T):
        if SEQ[x] % 2 == 0:
            M2 += 1
        if SEQ[x] % 3 == 0:
            M3 += 1
        if SEQ[x] % 4 == 0:
            M4 += 1
        if SEQ[x] % 5 == 0:
            M5 += 1
    print("{} Multiplo(s) de 2\n{} Multiplo(s) de 3\n{} Multiplo(s) de 4\n{} Multiplo(s) de 5".format(M2,M3,M4,M5))
else:
    quit()
