A = list(map(int,input().split()))
A.sort()
if A[0] == A[1] or A[2] == A[1] or A[0] == A[2]:
    print("S")
elif (A[2] - A[1] - A[0]) == 0:
    print("S")
elif (A[1] + A[0]) == A[2]:
    print("S")
else:
    print("N")
