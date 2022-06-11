ANDARES,INICIO,META,CIMA,BAIXO = map(int,input().split())
c = 0
for x in range(META):
    if INICIO < META:
        INICIO+= CIMA
        c += 1
    if INICIO > META:
        INICIO -= BAIXO
        c += 1
print(c)
