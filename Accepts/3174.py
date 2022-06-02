N_ELFOS,b,a,m,d = int (input()),0,0,0,0
for x in range(N_ELFOS):
    NOME = input().split()
    N,G,H = NOME
    if G == "bonecos":
        b += int(H)
    elif G == "arquitetos":
        a += int(H)
    elif G == "musicos":
        m += int(H)
    else:
        d += int(H)
print("{}".format(b//8 + a//4 + m//6 + d//12))
