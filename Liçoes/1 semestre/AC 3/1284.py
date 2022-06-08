TESTES,NOTAS,REPO,FINAL,ALT = int(input()),[],[],[],0
for x in range(TESTES):
    NOTAS.append(float(input()))
for i in range(TESTES):
    REPO.append(float(input()))
for j in range(TESTES):
    if NOTAS[j] == REPO[j] or REPO[j] == 0 or REPO[j] < 10: FINAL.append(NOTAS[j])
    if NOTAS[j] < REPO[j] and REPO[j] == 10:
        FINAL.append(NOTAS[j]+2)
        ALT += 1
for m in range(TESTES):
    if FINAL[m] > 10: FINAL[m] = 10
print("NOTAS ALTERADAS: {}".format(ALT))
for F in range(TESTES):
    if NOTAS[F] == FINAL[F]:print("-(00{}) original: {:05.2f} | final: {:05.2f}".format(F+1,NOTAS[F],FINAL[F]))
    else:print("*(00{}) original: {:05.2f} | final: {:05.2f}".format(F+1,NOTAS[F],FINAL[F]))
