def soma(sequencia):
    soma = 0
    for x in sequencia:
        soma += x
    return soma
N_TESTE = int(input())
for x in range(N_TESTE):
    NOME,GRAU,NOTAS = input(),float(input()),list(map(float,input().split()))
    NOTAS.sort()
    NOTAS.pop(0)
    NOTAS.pop(len(NOTAS)-1)
    print("{} {:.2f}".format(NOME,soma(NOTAS)*GRAU))
