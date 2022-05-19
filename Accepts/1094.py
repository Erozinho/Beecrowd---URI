N = int(input())
T, R, S, C = 0, 0, 0, 0
for X in range(N):
    QNUM,TIPO = input().split()
    QNUM = int(QNUM)
    T = T + QNUM
    if TIPO == "C":
        C = C + QNUM
    elif TIPO == "R":
        R = R + QNUM
    elif TIPO == "S":
        S = S + QNUM
print("Total: {} cobaias\nTotal de coelhos: {}\nTotal de ratos: {}\nTotal de sapos: {}".format(T,C,R,S,))
print("Percentual de coelhos: {:.2f} %\nPercentual de ratos: {:.2f} %\nPercentual de sapos: {:.2f} %".format(float(((C * 100) / T)),float(((R * 100) / T)),float(((S * 100) / T)),))
