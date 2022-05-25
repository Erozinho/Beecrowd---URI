def S(n1):
    soma = 0
    for i in range(12):
        soma += L12[n1][i]
    return soma
    
def M(n1):
    media = 0
    soma = 0
    for i in range(12):
        soma += L12[n1][i]
    media = soma/12
    return media

L12 = [
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0]
]
n,OP = int(input()),input()
for a in range(12):
    for i in range(12):
        NUM = float(input())
        L12[a][i] = NUM
if OP == "S":
    r1 = S(n)
    print("{:.1f}".format(r1))
if OP == "M":
    r2 = M(n)
    print("{:.1f}".format(r2))
