N,PM,PJ = int(input()),0,0
for X in range(N):
    j = 0
    while j < 3: 
        J1,J2 = map(int,input().split())
        PJ = J1 * J2;
        M1,M2 = map(int,input().split())
        PM = M1 * M2;
        j += 1
    if PJ > PM:
        print("JOAO")
    else:
        print("MARIA")
