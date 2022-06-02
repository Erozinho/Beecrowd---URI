N_T = int(input())
for x in range(N_T):
    N_BONUS = int(input())
    DABRI = list(map(int,input().split()))
    GUART = list(map(int,input().split()))
    ATQD = (DABRI[0]+DABRI[1])/2
    ATQG = (GUART[0]+GUART[1])/2
    if DABRI[2] % 2 == 0:
        ATQD = ATQD + N_BONUS
    if GUART[2] % 2 == 0:
        ATQG = ATQG + N_BONUS
    if ATQD > ATQG:
        print("Dabriel")
    elif ATQD < ATQG:
        print("Guarte")
    else:
        print("Empate")
