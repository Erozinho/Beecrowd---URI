n,A,E,H,M,X = int(input()),0,0,0,0,0
for x in range(n):
    SER = input().split()
    NOME,RACA = SER
    if RACA == "A": A+=1
    if RACA == "E": E+=1
    if RACA == "H": H+=1
    if RACA == "M": M+=1
    if RACA == "X": X+=1
print("{} Hobbit(s)\n{} Humano(s)\n{} Elfo(s)\n{} Anao(s)\n{} Mago(s)".format(X,H,E,A,M))
