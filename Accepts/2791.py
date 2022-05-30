A = list(map(int,input().split()))
for x in range(len(A)):
    if A[x] == 1:
        print(A[x]+x)
