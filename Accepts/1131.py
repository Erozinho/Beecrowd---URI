EMPATE,JOGADAS,PONTOS_INTER,PONTOS_GREMIO = 0,1,0,0
while True:
        INTER_GOLS,GREMIO_GOLS = map(int,input().split())
        if INTER_GOLS > GREMIO_GOLS:
            PONTOS_INTER += 1
        elif INTER_GOLS < GREMIO_GOLS:
            PONTOS_GREMIO += 1
        else:
            EMPATE +=1
        DENOVO = int(input("Novo grenal (1-sim 2-nao)\n"))
        if DENOVO == 1:
            JOGADAS += 1
        elif DENOVO == 2:
            break
print("{} grenais\nInter:{}\nGremio:{}\nEmpates:{}".format(JOGADAS,PONTOS_INTER,PONTOS_GREMIO,EMPATE))
if PONTOS_GREMIO > PONTOS_INTER:
    print("Gremio venceu mais")
elif PONTOS_GREMIO < PONTOS_INTER:
    print("Inter venceu mais")
else:
    print("Nao houve vencedor")
