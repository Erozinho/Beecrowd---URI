NTESTE = int(input())
PADRAO = list(map(int,input().split()))
if NTESTE == 2 and PADRAO[0] == PADRAO[1]:P = 0
else:
    P = 1
    for i in range(1, NTESTE-1):
        if not ((PADRAO[i] < PADRAO[i-1] and PADRAO[i] < PADRAO[i+1]) or (PADRAO[i] > PADRAO[i-1] and PADRAO[i] > PADRAO[i+1])):
            P = 0
            break
print(P)
