TESTE= int(input())
for x in range(TESTE):
    LISTA = list(input().split())
    A,B = map(int,input().split())
    if LISTA[1] == "PAR" and (A+B)%2==0:print(LISTA[0])
    elif LISTA[1] == "IMPAR" and (A+B)%2!=0:print(LISTA[0])
    elif LISTA[3] == "PAR" and (A+B)%2==0:print(LISTA[2])
    elif LISTA[3] == "IMPAR" and (A+B)%2!=0:print(LISTA[2])
