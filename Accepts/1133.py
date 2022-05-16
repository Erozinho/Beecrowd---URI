X = int(input())
Y = int(input())
if X > Y:
    M = X
    X = Y
    Y = M
for N in range(X + 1,Y):
    if (N % 5 == 2) or (N % 5 == 3):
        print(N)
