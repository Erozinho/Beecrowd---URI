def S():
    soma = 0
    for a in range (12):
        for i in range(12):
            if i != 12:
                soma += L12[a][i+1]
            if i == 12:
                soma += L12[a][i]
    return soma
    
def M():
    media = 0
    soma = 0
    for a in range(12):
        for i in range(12):
            if i != 12:
                soma += L12[a][i+1]
            if i == 12:
                soma += L12[a][i]
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
OP = input()
for a in range(12):
    for i in range(12):
        NUM = float(input())
        L12[a][i] = NUM
if OP == "S":
    r1 = S()
    print("{:.1f}".format(r1))
if OP == "M":
    r2 = M()
    print("{:.1f}".format(r2))
