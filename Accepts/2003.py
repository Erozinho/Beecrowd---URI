while True:
    try:
        H,M = (map(int,input().split(":")))
        if H <= 6:
            print("Atraso maximo: {}".format(M*0))
        elif H == 7:
            print("Atraso maximo: {}".format(M))
        elif H == 8:
            print("Atraso maximo: {}".format(M+60))
        else:
            print("Atraso maximo: {}".format(120))
    except EOFError:
        break
