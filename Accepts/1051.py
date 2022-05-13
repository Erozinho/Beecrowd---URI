SALARIO = float(input())
if SALARIO <= 2000:
    print("Isento")
elif SALARIO > 2000 and SALARIO <= 3000:
    TAXA = SALARIO - 2000
    VALOR = TAXA * 0.08
    print("R$ {:.2f}".format(VALOR))
elif SALARIO > 3000 and SALARIO < 4500:
    TAXA = SALARIO - 3000
    VALOR = (TAXA * 0.18) + (1000 * 0.08)
    print("R$ {:.2f}".format(VALOR))
else:
    TAXA = SALARIO - 4500
    VALOR = (TAXA * 0.28) + (1000 * 0.08) + (1500 * 0.18)
    print("R$ {:.2f}".format(VALOR))
