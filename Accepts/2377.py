PISTA,PEDAGIO = map(int,input().split())
C_KM,PRECO_PED = map(int,input().split())
print("{:.0f}".format((PISTA * C_KM) + ((PISTA // PEDAGIO) * PRECO_PED)))
