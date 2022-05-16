n1, n2, n3, n4 = map(float,input().split())
m = ((n1 * 2) + (n2 * 3) + (n3 * 4) + n4) / 10
print("Media: {:.1f}".format(m))
if m >= 7.0:
    print("Aluno aprovado.")
if m < 5.0:
    print("Aluno reprovado.")
if 5.0 <= m <= 6.9:
    print("Aluno em exame.")
    y = float(input())
    print("Nota do exame: {}".format(y))
    m2 = (y + m) / 2
    if m2 >=5:
        print("Aluno aprovado.\nMedia final: {:.1f}".format(m2))
    else:
        print("Aluno reprovado.\nMedia final: {:.1f}".format(m2))
