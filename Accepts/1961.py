P,N = map(int,input().split())
if 1 <= P <= 5 and 2 <= N <= 100:
    ganhar,perder = 0,0
    ALT_C = list(map(int,input().split()))
    for x in range(N):
        if x < N-1:
            if (ALT_C[x] + P) >= ALT_C[x+1] and ALT_C[x] - ALT_C[x+1] <= P:
                ganhar += 1
            else:
                perder += 1
                print("GAME OVER")
                break
        else:
            if (ALT_C[x] + P) >= ALT_C[N-1] and ALT_C[x] - ALT_C[N-1] <= P:
                ganhar +=1
            else:
                perder += 1
                print("GAME OVER")
                break
if perder == 0:
    print("YOU WIN")
