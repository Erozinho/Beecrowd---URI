A = int(input())
for X in range(A):
    N1, N2 , N3 = map(float,input().split())
    print("{:.1f}".format(((N1 * 2) + (N2 * 3) + (N3 * 5)) / 10))
