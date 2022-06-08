NUM_TESTE,CANAIS = int(input()),[]
for x in range(NUM_TESTE):
    CANAIS.append(input().split(";"))
P,C = float(input()),float(input())
print("-----\nBÔNUS\n-----")
for i in range(NUM_TESTE):
    if CANAIS[i][3] == "sim":print("{}: R$ {:.2f}".format(CANAIS[i][0],(int(CANAIS[i][1])//1000)*P + float(CANAIS[i][2])))
    else:print("{}: R$ {:.2f}".format(CANAIS[i][0],(int(CANAIS[i][1])//1000)*C + float(CANAIS[i][2])))
