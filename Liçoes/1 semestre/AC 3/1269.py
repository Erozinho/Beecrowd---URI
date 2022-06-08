NUM = list(map(int,input().split()))
NUM.sort()
while True:
    CMD = list(input().split())
    if CMD[0] == "encerrar":
        print(*NUM)
        quit()
    if CMD[0] == "exibir": print(*NUM)
    if CMD[0] == "adicionar":
        CMD[1] = int(CMD[1])
        NUM.append(CMD[1])
        NUM.sort()
    if CMD[0] == "remover":
        CMD[1] = int(CMD[1])
        if CMD[1] in NUM: NUM.remove(CMD[1])
        else:print("código {} não encontrado".format(CMD[1]))
