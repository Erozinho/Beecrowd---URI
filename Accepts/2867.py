n = int(input())
for x in range(n):
    n1,n2=map(int,input().split())
    A = n1**n2
    A = str(A)
    print(len(A))
