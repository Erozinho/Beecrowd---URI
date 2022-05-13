A, C, B, D = list(map(int,input().split()))
E = ((B * 60) + D) - ((A * 60) + C)
if E <= 0:
    E +=24*60
HR = E // 60
MIN = E % 60
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(HR, MIN))
