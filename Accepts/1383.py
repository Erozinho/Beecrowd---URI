def SUDOKU(matriz):
    for linha in matriz:
        check = [0] * 9
        for elemento in linha:
            check[elemento - 1] += 1
            if check[elemento - 1] > 1:return "NAO"
    return "SIM"
    
N_TESTE = int(input())
for x in range(N_TESTE):
    S = []
    for linha in range(9):S.append([int(i) for i in input().split()])
    saida = SUDOKU(S)
    print("Instancia {}".format(x+1))
    print(saida)
    print()
