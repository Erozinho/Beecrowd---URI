N_TESTES,TOTAL,NUMEROS = int(input()),0,[]
for X in range(N_TESTES):
    N = int(input())
    NUMEROS.append(N)
for i in range(N_TESTES):
    if i != N_TESTES - 1 and NUMEROS[i] == NUMEROS[i + 1]:
        pass
    elif i != (N_TESTES - 1) and NUMEROS[i] != NUMEROS[i + 1]:
        TOTAL += 1
    elif i == (N_TESTES - 1) and NUMEROS[i] == NUMEROS[i]:
        pass
    else:
        TOTAL += 1
print("{}".format(TOTAL+1))
