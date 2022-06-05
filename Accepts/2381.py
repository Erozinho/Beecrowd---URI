N,SELC = map(int,input().split())
ALUNOS = []
for x in range(N):
    A = input()
    ALUNOS.append(A)
ALUNOS.sort()
print(ALUNOS[SELC-1])
