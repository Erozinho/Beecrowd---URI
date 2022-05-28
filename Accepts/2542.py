while True:
    try:
        N_ATRIBUTO = int(input())
        CARTAS_M,CARTAS_L = map(int,input().split())
        for x in range(CARTAS_M):
            globals()["C{}M".format(x)] = list(map(int,input().split()))
        for i in range(CARTAS_L):
            globals()["C{}L".format(i)] = list(map(int,input().split()))
        if len(C0M) == len(C0L) == N_ATRIBUTO:
            SELECT_CM,SELECT_CL = map(int,input().split())
            NUM_ATRI = int(input())
            if globals()["C{}M".format(SELECT_CM-1)][NUM_ATRI-1] > globals()["C{}L".format(SELECT_CL-1)][NUM_ATRI-1]:
                print("Marcos")
            elif globals()["C{}M".format(SELECT_CM-1)][NUM_ATRI-1] < globals()["C{}L".format(SELECT_CL-1)][NUM_ATRI-1]:
                print("Leonardo")
            else:
                print("Empate")
        else:
            break
    except EOFError:
        break
