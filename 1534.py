while True:
    try:
        NUMERO,matriz = int(input()),[]
        for x in range(NUMERO):
            matriz.append([])
            for i in range(NUMERO):
                matriz[x].append("3")
            c1 = NUMERO - 1
        for x in range(NUMERO):
            matriz[x][x] = "1"
            matriz[x][c1] = "2"
            c1 -= 1
            lista = ''.join(matriz[x])
            print(lista)
    except EOFError:
        break
