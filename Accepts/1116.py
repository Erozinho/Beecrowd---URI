N = int(input())
for I in range(N):
    X,Y = map(int,input().split())
    if Y == 0:
        print("divisao impossivel")
    else:
        print("{:.1f}".format(X / Y))
        
