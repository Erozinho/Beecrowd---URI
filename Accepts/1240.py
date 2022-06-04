NUM_TESTE = int(input())
for x in range(NUM_TESTE):
    A,B = input().split()
    if len(B) > len(A):
        print("nao encaixa")
    else:
        if A[len(A) - len(B): len(A)] == B:
            print("encaixa")
        else:
            print("nao encaixa")
