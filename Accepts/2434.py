DIAS,SALDO_INICIAL = map(int,input().split())
VALORES = []
for X in range(DIAS):
    VALOR,temp = int(input()),0
    if VALOR < 0:
        SALDO_INICIAL = SALDO_INICIAL + (VALOR)
        VALORES.append(SALDO_INICIAL)
    else:
        SALDO_INICIAL = SALDO_INICIAL + VALOR
        VALORES.append(SALDO_INICIAL)
VALORES.sort()
print(VALORES[0])
