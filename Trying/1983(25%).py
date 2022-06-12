QTD,ALUNOS,PASS = int(input()),[],[]
for x in range(QTD):ALUNOS.append(input().split())
for i in range(2):
    if float(ALUNOS[i][1]) >= 8: PASS.append(ALUNOS[i][0])
PASS.sort()
if len(PASS) > 0:print(PASS[len(PASS)-1])
else:print("Minimum note not reached")
