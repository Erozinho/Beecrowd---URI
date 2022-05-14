while True:
    try:
        N = int(input())
        EPR, EHD, INTRUSOS = 0, 0, 0
        for X in range(N):
            RM,CURSO = input().split()
            RM = int(RM)
            if CURSO == "EPR":
                EPR += 1
            elif CURSO == "EHD":
                EHD += 1
            else:
                INTRUSOS += 1
        print("EPR: {}\nEHD: {}\nINTRUSOS: {}".format(EPR,EHD,INTRUSOS))
    except EOFError:
        break
