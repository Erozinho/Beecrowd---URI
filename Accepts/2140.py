NOTAS = [2,5,10,20,50,100]
while True:
    DA = False
    N,M = map(int,input().split())
    if N == M == 0:
        break
    for i in range(len(NOTAS)):
        for j in range(len(NOTAS)):
            if (M-N) - NOTAS[j] == NOTAS[i]:
                DA = True
    if DA == True:
        print("possible")
    else:
        print("impossible")
