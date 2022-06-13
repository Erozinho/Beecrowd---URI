N_TESTE = int(input())
for x in range(N_TESTE):
    A = input().split("+")
    if len(A) < 2:print("skipped")
    else: print("{}".format(int(A[0])+int(A[1])))
