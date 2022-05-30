OP,MATRIZ = input(),[]
for X in range(12):
    MATRIZ.append([])
    for j in range(12):
        x = float(input())
        MATRIZ[X].append(x)
SOMA,CONTROLE,C = 0,0,11
for i in range(1,11):
    for X1 in range(C,12):
        SOMA += MATRIZ[i][X1]
        CONTROLE += 1
    if i < 5:
        C -= 1
    if i > 5:
        C += 1
MEDIA = (SOMA / CONTROLE)
if OP == "S":
    print("{:.1f}".format(SOMA))
else:
    print("{:.1f}".format(MEDIA))
