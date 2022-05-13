A = int(input())
for X in range(1, A + 1):
    NUM = input().split()
    N1, N2 , N3 = NUM
    N1 = float(N1)
    N2 = float(N2)
    N3 = float(N3)
    print("{:.1f}".format(((N1 * 2) + (N2 * 3) + (N3 * 5)) / 10))
