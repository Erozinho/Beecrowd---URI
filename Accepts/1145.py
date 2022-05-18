X,Y = list(map(int,input().split()))
C = 1
for i in range(1,(int((Y/X))+1)):
    A = ""
    for d in range(X):
        A += str(C) + " "
        C += 1
    print(A[:-1])
