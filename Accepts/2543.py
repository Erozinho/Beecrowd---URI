while True:
    try:
        N_TESTE, ID_FACU = map(int,input().split())
        c = 0
        for x in range(N_TESTE):
            ID_ALUNO,JOGO = map(int,input().split())
            if JOGO == 0 and ID_ALUNO == ID_FACU:
                c += 1
        print(c)
    except EOFError:
        break
