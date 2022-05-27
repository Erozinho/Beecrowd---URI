def NCARTASS(N1, N2):
    resto = 1
    while resto != 0:
        resto = N1 % N2
        N1 = N2
        N2 = resto
    return N1

N = int(input())
for x in range(N):
    F1,F2 = map(int,input().split())
    print(NCARTASS(F1, F2))
