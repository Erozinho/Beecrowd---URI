NUM_ABAS,ACOES = map(int,input().split())
for x in range(ACOES):
    ACAO = input()
    if ACAO == "fechou":
        NUM_ABAS += 1
    if ACAO == "clicou":
        NUM_ABAS -= 1
print(NUM_ABAS)
