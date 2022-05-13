SALARIO = float(input())
PER = 0
if SALARIO >= 0 and SALARIO <= 400:
    PER = 0.15 * SALARIO
    print("Novo salario: {:.2f}".format(PER + SALARIO))
    print("Reajuste ganho: {:.2f}".format(PER))
    print("Em percentual: {} %".format(15))
if SALARIO >= 400.01 and SALARIO <= 800:
    PER = 0.12 * SALARIO
    print("Novo salario: {:.2f}".format(PER + SALARIO))
    print("Reajuste ganho: {:.2f}".format(PER))
    print("Em percentual: {} %".format(12))
if SALARIO >= 800.01 and SALARIO <= 1200:
    PER = 0.10 * SALARIO
    print("Novo salario: {:.2f}".format(PER + SALARIO))
    print("Reajuste ganho: {:.2f}".format(PER))
    print("Em percentual: {} %".format(10))
if SALARIO >= 1200.01 and SALARIO <= 2000:
    PER = 0.07 * SALARIO
    print("Novo salario: {:.2f}".format(PER + SALARIO))
    print("Reajuste ganho: {:.2f}".format(PER))
    print("Em percentual: {} %".format(7))
if SALARIO > 2000:
    PER = 0.04 * SALARIO
    print("Novo salario: {:.2f}".format(PER + SALARIO))
    print("Reajuste ganho: {:.2f}".format(PER))
    print("Em percentual: {} %".format(4))
