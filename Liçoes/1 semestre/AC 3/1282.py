NUM_TESTE,CANAIS = int(input()),[]
for x in range(NUM_TESTE):
    CANAIS.append(input().split(";"))
    CANAIS[x][1] = int(CANAIS[x][1])
    CANAIS[x][2] = float(CANAIS[x][2])
P,C = float(input()),float(input())
print("-----\nBÔNUS\n-----")
for i in range(NUM_TESTE):
    if CANAIS[i][3] == "sim":print("{}: R$ {:.2f}".format(CANAIS[i][0],(CANAIS[i][1]//1000)*P + CANAIS[i][2]))
    else:print("{}: R$ {:.2f}".format(CANAIS[i][0],(CANAIS[i][1]//1000)*C + CANAIS[i][2]))
