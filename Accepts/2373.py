TESTES = int(input())
Q = 0
for x in range(TESTES):
    L,C = map(int,input().split())
    if L > C:
        Q += C
print(Q)
