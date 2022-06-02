N_T = int(input())
for x in range(N_T):
    RELOGIO = list(map(int,input().split()))
    if RELOGIO[2] == 0:
        print("{:02}:{:02} - A porta fechou!".format(RELOGIO[0],RELOGIO[1]))
    else:
        print("{:02}:{:02} - A porta abriu!".format(RELOGIO[0],RELOGIO[1]))
