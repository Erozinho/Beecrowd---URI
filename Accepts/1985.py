N_COMPRAS,A,VALORES = int(input()),0,{1001:1.50,1002:2.50,1003:3.50,1004:4.50,1005:5.50}
for X in range(N_COMPRAS):
    ID,QTD = map(int,input().split())
    A = (VALORES[ID]*QTD) + A
print("{:.2f}".format(A))
