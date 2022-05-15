N = int(input())
B = 0
for A in range(N):
    I = 0
    X, Y = map(int,input().split())
    B = 0
    if X > Y:
        for I in range((Y+1),X):
            if (I % 2 != 0):
                B += I
    if Y > X:
        for I in range((X+1),Y):
            if (I % 2 != 0):
                B += I
    else:
        B == 0
    print(B)
